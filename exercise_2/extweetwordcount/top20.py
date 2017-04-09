import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


# Establish connection
conn = psycopg2.connect(database="tcount",user="postgres",password="pass",host="localhost",port="5432")
cur = conn.cursor()
# Select all
cur.execute("SELECT word, count from tweetwordcount order by count desc limit 20")
records = cur.fetchall()

print "top 20 words\n"
for rec in records:
       print "%s : %s" % (rec[0],rec[1])

conn.commit()
conn.close()
