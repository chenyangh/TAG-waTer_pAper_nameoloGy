from nltk import FreqDist
from nltk.corpus import brown
from nltk.corpus import stopwords
import nltk
import string
import argparse
parser = argparse.ArgumentParser(description='Options')
parser.add_argument('-bin', default=1000, type=int,
                    help="the number of frequent words you are searching from")
parser.add_argument('-title', default='Water Paper Nameology', type=str,
                    help="tile of the paper")
opt = parser.parse_args()


nltk.download('stopwords')
nltk.download('brown')

BIN_SIZE = opt.bin
TITLE = opt.title

stopwords = list(stopwords.words('english'))

frequency_list = FreqDist(i.lower() for i in brown.words())

freq_words = frequency_list.most_common()[:BIN_SIZE]

freq_words = [item[0] for item in freq_words]

freq_words_no_stopwords = [value for value in freq_words
                           if value not in stopwords and value[0] not in string.punctuation]


water_paper_name = TITLE.lower().strip()

old_water_paper_name = water_paper_name

water_paper_name = ' '.join([x for x in water_paper_name.split() if x not in stopwords])

stopwords_water_paper_name = [(i, x)for i, x in enumerate(old_water_paper_name.split())
                              if x in stopwords]

water_paper_name_combined = ''.join([x for x in water_paper_name.split()])


def is_subseq(x, y):
    """
    Find from https://stackoverflow.com/questions/24017363/how-to-test-if-one-string-is-a-subsequence-of-another
    """
    it = iter(y)
    return all(c in it for c in x)


matched_words = [word for word in freq_words_no_stopwords if is_subseq(word, water_paper_name_combined)]

# print(matched_words)


def align_water_style(cand, paper_name):
    def find_all_index(cand_str, target_str):
        return [i for i, x in enumerate(target_str) if x == cand_str]
    aligned = {}
    for i, char in enumerate(cand):
        aligned[i] = []
        for j, word in enumerate(paper_name.split()):
            all_index = find_all_index(char, word)
            if len(all_index) > 0:
                for idx in all_index:
                    aligned[i].append((j, idx))
    return aligned


def match_water_style(cand, paper_name):
    """
    We want each word in the tile contains at least one of the character in its shorten name (WATER STYLE).
    """
    aligned = align_water_style(cand, paper_name)

    path_list = []

    for idx_cand in range(len(cand)):
        next_path_list = []
        for match in aligned[idx_cand]:
            next_path_list.append(match)
        if len(path_list) == 0:
            path_list.append(next_path_list)
        else:
            new_patch_list = []
            for path in path_list:
                for next_path in next_path_list:
                    new_patch_list.append(path + [next_path])

            path_list = new_patch_list

    # find if a valid path exists
    for path in path_list:
        possible_path = [y[0] for y in path]
        if sorted(possible_path) == possible_path:
            if is_subseq(list(range(len(paper_name.split()))), possible_path):
                if len(path) == len(set(path)):
                    if len(path) != len(cand):
                        break

                    flag = False
                    for i in range(len(paper_name.split())):
                        tmp = []
                        for j in path:
                            if j[0] == i:
                                tmp.append(j[1])
                        if sorted(tmp) != tmp:
                            flag = True
                            break
                    if not flag:
                        # print MATCHED
                        title_list = paper_name.split()

                        new_words = [list(x) for x in title_list]

                        for p in path:
                            new_words[p[0]][p[1]] = new_words[p[0]][p[1]].upper()

                        new_words = [''.join(x) for x in new_words]

                        # print('before,', ' '.join(new_words))
                        for i, s in stopwords_water_paper_name:
                            # print('inserting', i, s)
                            new_words.insert(i, s)

                        print(cand.upper(), ':', ' '.join(new_words))
                        return True

    return False


for word in matched_words:
    match_water_style(word, water_paper_name)
# match_water_style('tag', water_paper_name)

