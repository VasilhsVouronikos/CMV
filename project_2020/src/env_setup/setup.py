import subprocess
import sys,os
import pip



def get_required_packages():
	if(sys.platform == "linux" or sys.platform == "Linux"):
		with open(os.getcwd()+"/required_pack.txt","r") as req:
			modules = []
			for lines in req:
				line = lines.strip("\n").split("=")
				modules.append(line[1])
	else:
		with open(os.getcwd()+"\\required_pack.txt","r") as req:
			modules = []
			for lines in req:
				line = lines.strip("\n").split("=")
				modules.append(line[1])

	return modules

def install_package():
	packages = get_required_packages()
	for pack in packages:
		try :
			import pack
		except:
			res = subprocess.run(["pip3", "install",pack])
                        

print("Installing packages ...")
print(sys.platform)
install_package()
