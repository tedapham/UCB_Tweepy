from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

# Added library for Postgres communications
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        # Connect to database tcount
        self.conn = psycopg2.connect(database="tcount",user="postgres",password="pass",host="localhost",port="5432")
        
    def process(self, tup):
        # Get word, convert it to string
        word = str(tup.values[0])

        # Set cursor  
        cur = self.conn.cursor()

        # Icrement wordcount in tweetwordcount table if the word already exists in the table
        cur.execute("UPDATE tweetwordcount SET count = count+1 WHERE word = %s",(word,))

        # if word is not in the table, add word and count of 1
        if cur.rowcount == 0:
            cur.execute("INSERT INTO tweetwordcount (word, count) VALUES (%s,1)",(word,))
        
        self.conn.commit()

        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))
