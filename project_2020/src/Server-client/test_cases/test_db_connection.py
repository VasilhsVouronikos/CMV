# in this script we test if we connect with the database correctly
# if we succesfully connect a varification massage will be printed in the console
# else we will get a "unable to connect" massage
import sys
import os

def get_current_path():
	path = os.getcwd().split("/")
	path.pop(0)
	path.pop(len(path)-1)
	new_path = "/"+"/".join(path)
	
	return new_path

path_to_database = get_current_path()

sys.path.insert(0,path_to_database)

from db_connect import Connector


def test_db_connection():
	try:
		conn = Connector()
		cursor = conn.create_cursor()
	except:
		print("unable to connect")

test_db_connection()