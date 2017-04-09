import sys
import psycopg2

#Connecting to tcount
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()


if len(sys.argv) == 1:
    # Print Final Results Table as a set of tuples
    cur.execute("SELECT word, count from tweetwordcount ORDER BY count desc, word asc")
    records = cur.fetchall()
    for rec in records:
       print "word = ", rec[0]
       print "count = ", rec[1], "\n"

elif len(sys.argv) > 1:
    # Print count of input words
    for i in range(len(sys.argv)-1):
        word = sys.argv[i+1]
        # get count from table
	cur.execute("SELECT count from tweetwordcount where word = %s", (word,))
        count = cur.fetchall()

        print'Total number of occurrences of "' + word + '": ', count[0][0]

conn.commit()
conn.close()
