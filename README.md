# Twitter follow-bot identifier

Program will automatically identify follow-bots for any given Twitter account using Twitter API 
and the Tweepy library. 
 <br/>

Default is Twitter's official account, `@twitter` (can be modified directly in the code).
 <br/>

The program will go through up to 40 followers (can be mofidied directly in the code) of @twitter and if any of them meet all of the conditions
(typically found in a follow-bot) that have been set, then it is assumed that 
they are a follow-bot.
<br/>

To improve: <br/>
can set more specific condition to determine a follow-bot (e.g. if the twitter name 
have a series of numbers or check if their DMs are empty). <br/>
ask for user input to change the default account and the number of identified follow-bots
<br/>

note: removed keys for security<br/>
================= Example script running =================<br/>

Examining @<twitterhandle>...<br/>
Examining @<twitterhandle>...<br/>
Examining @<twitterhandle>...<br/>
Examining @<twitterhandle>...<br/>
Examining @<twitterhandle>...<br/>
Examining @<twitterhandle>...<br/>
Examining @<twitterhandle>...<br/>
Examining @<twitterhandle>...<br/>
Found follow-bot #1: twitter.com/<followbot-twitterhandle><br/>
Examining @<twitterhandle>...<br/>
Examining @<twitterhandle>...<br/>
Found follow-bot #2: twitter.com/<followbot-twitterhandle><br/>
...<br/>
