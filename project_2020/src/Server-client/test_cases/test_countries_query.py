#in this test we will run queries_from_countries function
#of db_connect to test if country codes are returned correctly


import sys
import os

global conn


def get_current_path():
	path = os.getcwd().split("/")
	path.pop(0)
	path.pop(len(path)-1)
	new_path = "/"+"/".join(path)
	
	return new_path

path_to_database = get_current_path()

sys.path.insert(0,path_to_database)

from db_connect import Connector


def connect_to_db():
	global conn
	try:
		conn = Connector()
		cur = conn.connect()
	except:
		print("unable to connect")
	


def test_countries_query():
	global conn
	connect_to_db()

	list1 = ("Greece\r","Germany\r")
	list2 = ("Kenya\r","Japan\r","India\r")

	result1 = conn.queries_from_countries(list1)
	result2 = conn.queries_from_countries(list2)

	print("output country code for first set with country list = ",list1,"is:","\n")
	for i in result1:
		print(i)

	print("output country code for second set with country list = ",list2,"is:","\n")
	for j in result2:
		print(j)



test_countries_query()