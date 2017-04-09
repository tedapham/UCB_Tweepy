import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def check_user_input():
	if len(sys.argv) == 2:
		key = sys.argv[1]
	elif len(sys.argv) > 2:
		print ("Please only input only one word")
		key = None
	else:
		key = "All"
	return key

# Check for user input
user_input = check_user_input()

if user_input != None:
	# Establish connection
	conn = psycopg2.connect(database="tcount",user="postgres",password="pass",host="localhost",port="5432")
	cur = conn.cursor()

	# Select all
	cur.execute("SELECT word, count from tweetwordcount")
	records = cur.fetchall()

	word_list = dict()
	conn.commit()
	conn.close()
	for rec in records:
		word_list[rec[0]] = rec[1]

	if user_input == "All":
		print "Words sorted alphabetically and their occurrence count in the Tweeter Stream"
		for key in sorted(word_list):
			print "%s : %s" % (key,word_list[key])

	else:
		try:
			print "Total number of occurrences of %s is : %s" %(user_input,word_list[user_input])
		except:
			print "%s was not found in tweetwordcount" % (user_input)




