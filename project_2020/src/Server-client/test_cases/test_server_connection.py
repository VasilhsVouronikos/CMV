# in this script we simply test that server runs in localhost 0.0.0.0 in port 5000
import sys
import os

def get_current_path():
	path = os.getcwd().split("/")
	path.pop(0)
	path.pop(len(path)-1)
	new_path = "/"+"/".join(path)
	
	return new_path

path_to_server = get_current_path()

sys.path.insert(0,path_to_server)

from server import start_server

def test_connection():
	try:
		start_server()
	except:
		print("unable to establishe connection")




test_connection()