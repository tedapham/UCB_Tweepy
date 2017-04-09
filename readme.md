# LIVE TWITTER STREAM ANALYSIS

## UCB W205 DATA STORAGE AND RETRIEVAL | by TED PHAM | April 9, 2017

## APPLICATION SUMMARY

The application captures, processes, and stores live tweets and in &quot;&lt;word&gt;: count&quot; form in a Postgres database. This process runs continuously until user&#39;s termination input (Ctrl+c) is received. Analyses of the captured words and their occurrences can be performed by calling the accompanying Python serving scripts which are described in details in the following file structure section.

The codes were developed and tested to be fully functional in a Linux environment from Amazon Web Services EC2 instance of UCB&#39;s community AMI UCB MIDS W205 EX2-FULL. The AMI provides the required technologies for the application: 1. **HDFS** ; 2. **Storm** ; 3. **Postgres** ; 4. **PsycoPG** ; 5. **Tweepy** ; 6. **Python** 2; 7. **Streamparse**.

## APPLICATION TOPOLOGY



The application topology is the crucial component in capturing and real-time processing of twitter data. A tweet-spout pulls tweets from Twitter streaming API and runs on three threads. Users can obtain their own twitter credentials for the tweet-spout by creating a twitter application at [https://apps.twitter.com](https://apps.twitter.com) . For convenience, a set of working credentials is provided. While the tweet-spout retrieves raw tweets, the two bolts parse-tweet-bolt and count-bolt processes tweets to valid words and counts the word respectively. In addition, the count-bolt also pushes and updates the data into a Postgres database. The Postgres database is initiated before each application is ran and contains only the tweets data of each individual run.

The database is called tcount with data stored in a table called tweetwordcount.

## FILE STRUCTURE

The application files are stored in the following Github repository

[https://github.com/tedapham/UCB\_Tweepy.git](https://github.com/tedapham/UCB_Tweepy.git) , containing exercise\_2 folder. The file structure described below is from within this exercise\_2 folder.

| **Name of the program** | **Location** | **Description** |
| --- | --- | --- |
| extweetwordcount.clj | extweetwordcount/topologies/ | topology for the application |
| tweets.py | extweetwordcount/src/spouts/ | tweet-spout |
| parse.py | extweetwordcount/src/bolts/ | parse-tweet-bolt |
| initialize.py | extweetwordcount/ | Create a fresh Postgres databaseNeeds to be run before the application |
| finalresults.py | extweetwordcount/ | When passed a single word as an argument, returns the total number of word occurrences in the stream. Without an argument returns all the words in the stream, and their total count of occurrences, sorted alphabetically, one word per line.  |
| histogram.py | extweetwordcount/ | Gets two integers k1,k2 and returns all the words with a total number of occurrences between k1,k2 |
| top20.py | extweetwordcount/ | returns 20 words with the largest number of occurrences |
| plot.png | /exercise\_2 | Plot of top 20 words |
| README.txt | /exercise\_2 | Execution Instructions |



## EXECUTION INSTRUCTIONS

Whether the UCB&#39;s community AMI is used, make sure the seven platforms highlighted in the application summary are installed and Postgres server running on the respective Linux platform. Once the repo is cloned, navigate to extweetwordcount subfolder inside UCB\_Tweepy/exercise\_2.

Run the application as followed:

$ python initialize.py

$ sparse run

**initialize.py must be run** to create tcount database and tweetwordcount table in Postgres before sparse can be run.

Once the application is run successfully, a continuous log will be displayed such as this:

Stop the process with ctrl+ c. At this point, twitter data have been tabulated in Postgres table twitterwordcount.

Running finalresults.py, histogram.py, and top20.py for analyses. For example:
