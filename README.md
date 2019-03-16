# TAG: waTer pAper nameoloGy ​​​​

TAG is a tool to help you find a name for your paper which matches the *WATER STYLE*

Given a string X and a title Y, X is referred as the *WATER STYLE* subsequence of Y if:
1. X is a frequently used English word.
2. Each word in Y must have at least one character that appear in X.
3. X is a subsequence of Y.

There are currently two supported arguments currently:
-bin: the number of most frequent words in nltk's *brown* corpora that will be considered.
-title: the title of the paper 

```
python TAG.py -bin=10000 -title="Water Paper Nameology"
```
Would yield the following matches:

WAY : Water pAper nameologY

TEN : waTer papEr Nameology

TRY : waTer papeR nameologY

TEAM : waTEr pAper naMeology

TERM : waTEr papeR naMeology

WARM : WAter papeR naMeology

TREE : waTeR papEr namEology

TAPE : waTer pAPer namEology

TEA : waTer papEr nAmeology

TRAY : waTeR pAper nameologY

WEARY : WatEr pApeR nameologY

WARN : WAter papeR Nameology

TAN : waTer pAper Nameology

WARMLY : WAter papeR naMeoLogY
