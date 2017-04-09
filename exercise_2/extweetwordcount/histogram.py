import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def check_user_input():
	lower_bound, upper_bound = 0,0
	if len(sys.argv) == 2:
		user_input = sys.argv[1]
		try:
			user_input = user_input.split(",")
			lower_bound = int(user_input[0])
			upper_bound = int(user_input[1])
			if lower_bound > upper_bound:
				print "please input lowerbound first"
				valid = False
			else:
				valid = True
		except:
			print "please input lower and upper bounds for occurrences in form of 'integer1,integer2'"
			valid = False
	else:
		print "Please input lower and upper bounds for occurences in form of 'integer1, integer2'"
		valid = False
	return (valid,lower_bound,upper_bound)

# Check for user input
user_input = check_user_input()

if user_input[0]:
	# Establish connection
	conn = psycopg2.connect(database="tcount",user="postgres",password="pass",host="localhost",port="5432")
	cur = conn.cursor()

	# get bounds
	lower_bound = user_input[1]
	upper_bound = user_input[2]

	# get max count

	cur.execute("SELECT MAX(count) FROM tweetwordcount")
	max_count = cur.fetchone()[0]
	
	# Check if lowerbound is less than max_count
	if int(max_count) < lower_bound:
		print "No word has occurence that falls between %s and %s" %(str(lower_bound),str(upper_bound))
	else:
	# Select depending on bounds
	
		if lower_bound == upper_bound:
			cur.execute("SELECT word, count FROM tweetwordcount WHERE count = " + str(lower_bound))
		else:
			cur.execute("SELECT word, count FROM tweetwordcount WHERE count BETWEEN %s AND %s",(str(user_input[1]),str(user_input[2])))
	
	# fetch data
	
		records = cur.fetchall()
		if len(records) == 0:
			print "There is nothing"
		else:
			for rec in records:
				print "%s: %s" %(rec[0],rec[1])

	conn.commit()
	conn.close()



