import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
conn = psycopg2.connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432")

try:
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute("DROP DATABASE IF EXISTS tcount")
    cur.execute("CREATE DATABASE tcount")
    cur.close()
    conn.close()
    print "database tcount created"
except:
	print "Could not create database tcount"

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

#Create a Table
#The first step is to create a cursor. 

try:
	cur = conn.cursor()
	cur.execute("DROP TABLE IF EXISTS tweetwordcount")
	cur.execute('''CREATE TABLE tweetwordcount
		(word TEXT PRIMARY KEY NOT NULL,
		count INT NOT NULL);''')
	conn.commit()
	cur.close()
	conn.close()
	print "sucessful table tweet"
except:
	print "Could not create table tweet"
