#in this test we will run get_years function
#of db_connect to test if year groups are returned correctly


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
	


def test_year_groups():
	global conn
	connect_to_db()

	test_period1 = "5"
	test_year1 = "1980"

	test_period2 = "10"
	test_year2 = "1967"

	test_period3 = "1"
	test_year3 = "2007"

	result1 = conn.get_years(test_period1,test_year1)
	result2 = conn.get_years(test_period2,test_year2)
	result3 = conn.get_years(test_period3,test_year3)

	print("output for first set with year = ",test_year1,"and period = ",test_period1,"is:","\n")
	for i in result1:
		print(i)

	print("output for second set with year = ",test_year2,"and period = ",test_period2,"is:","\n")
	for j in result2:
		print(j)

	print("output for second set with year = ",test_year3,"and period = ",test_period3,"is:","\n")
	for k in result3:
		print(k)


test_year_groups()