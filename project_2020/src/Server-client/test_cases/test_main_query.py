# in this test we will run the main function of db_connector
# which is excecute_query
# this test also tests queries_from_indicators which answers the query
# by calling the rest of the functions of db_connect

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
		cursor = conn.connect()
	except:
		print("unable to connect")
	return cursor

def test_queries():
	global conn
	connect_to_db()
	# this data represents the format of the input client data that the server receives and proscesses
	data1 = ["Canada","Brazil","Merchandise imports by the reporting economy","Gross domestic savings"
	,"1980","5","line"]
	data2 = ["Canada","GDP deflator"
	,"1985","10","line"]
	data3 = ["Canada","Greece","Merchandise imports by the reporting economy"
	,"2000","1","scatter"]
	output1 = conn.excecute_query(data1)
	output2 = conn.excecute_query(data2)
	output3 = conn.excecute_query(data3)
	print("output for data 1\n")
	if(output1 == "no result"):
		print(output1)
	else:
		for i in output1:
			print(i)

	print("output for data 2\n")
	if(output2 == "no result"):
		print(output2)
	else:
		for i in output2:
			print(i)

	output3 = conn.excecute_query(data3)
	print("output for data 3")
	if(output3 == "no result"):
		print(output3)
	else:
		for i in output3:
			print(i)


test_queries()

