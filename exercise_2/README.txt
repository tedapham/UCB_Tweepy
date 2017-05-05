
**************************
* Execution Instructions * 
**************************


The codes were developed and tested in a Linux environment from Amazon Web Services EC2 instance of UCB’s community AMI UCB MIDS W205 EX2-FULL. The AMI provides the required technologies for the application: 1. HDFS; 2. Storm; 3. Postgres; 4. PsycoPG; 5. Tweepy; 6. Python 2; 7. Streamparse.


Whether the UCB’s community AMI is used, make sure the seven platforms highlighted in the application summary are installed and Postgres server running on the respective Linux platform. 


Once the repo is cloned, 
****NAVIGATE to extweetwordcount**** 
subfolder inside UCB_Tweepy/exercise_2.

================================
Run the application as followed:
================================
$ python initialize.py
$ sparse run

initialize.py must be run to create tcount database and tweetwordcount table in Postgres before sparse can be run.

Once the application is run successfully, a continuous log will be displayed.
Stop the process with ctrl+c when the desired duration is reached. 

At this point, twitter data have been tabulated in Postgres table twitterwordcount.

================================
How to run finalresults.py
================================

$python finalresults.py <word>

if passed an argument
finalresults.py will display the count for the word passed
if no argument
finalresults.py will return words (sorted alphabetically) and their counts

================================
How to run histogram.py
================================

$python histogram.py k1,k2

k2 >= k1
return words with count between [k1,k2]

================================
How to run top20.py
================================

$python top20.py
return 20 words with top counts

