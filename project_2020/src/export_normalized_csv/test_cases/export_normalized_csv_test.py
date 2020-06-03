import sys

def get_current_path():
	path = os.getcwd().split("/")
	path.pop(0)
	path.pop(len(path)-1)
	new_path = "/"+"/".join(path)
	
	return new_path

path = get_current_path()

sys.path.insert(0,path)

from proscess_data import load_to_base

def test_normalize_export_csv():
	try:
		load_to_base()
	except:
		print("unable to export normalized csv's")