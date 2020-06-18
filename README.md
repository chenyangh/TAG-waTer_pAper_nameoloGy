# TAG: waTer pAper nameoloGy ​​​​

TAG is a tool to help you find a name for your paper which matches the *WATER STYLE*

Given a string X and a title Y, X is referred as the *WATER STYLE* subsequence of Y if:
1. X is a frequently used English word.
2. Each word in Y must have at least one character that appears in X.
3. X is a subsequence of Y.

There are two supported arguments currently:
-bin: the number of most frequent words in nltk's *brown* corpora that will be considered.
-title: the title of the paper 

```
python TAG.py -bin=100000 -title="Water Paper Nameology"
```
would yield the following matches in a few seconds:

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
TERRY : waTER papeR nameologY
WARY : WAter papeR nameologY
TEEN : waTEr papEr Nameology
TEE : waTer papEr namEology
**TAG : waTer pAper nameoloGy**
WRY : Water papeR nameologY
TAME : waTer pAper naMEology
WEE : Water papEr namEology
TAO : waTer pAper nameOlogy
TANG : waTer pAper NameoloGy
TROY : waTer papeR nameOlogY
WATERY : WATEr papeR nameologY
WAN : Water pAper Nameology
TERRAL : waTER papeR nAmeoLogy
WAO : Water pAper nameOlogy
TANGY : waTer pAper NameoloGY
WARE : WAter papeR namEology
TERRA : waTER papeR nAmeology
TARA : waTer pApeR nAmeology
TERRAM : waTER papeR nAMeology
TEL : waTer papEr nameoLogy
WPA : Water Paper nAmeology

