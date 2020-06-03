import os,sys
import csv
import time
import re


try:
    directory = sys.argv[1]
except:
    directory = os.getcwd()+"/source_files/proscess_csv/test_cases/test_csv"


################
#give directory pf csv's as a terminal argument
################

indicator_list=["Trade (% of GDP)","Gross capital formation (% of GDP)","Exports of goods and services (% of GDP)","Merchandise exports by the reporting economy (current US$)",
"Merchandise imports by the reporting economy (current US$)","Merchandise trade (% of GDP)","Gross domestic savings (% of GDP)","Total natural resources rents (% of GDP)",
"GDP per capita growth (annual %)","GDP deflator (base year varies by country)","Exports as a capacity to import (constant LCU)","Energy imports, net (% of energy use)"]
final_csv_path=""
countries_data=[]
years=[]
csv_list=[]
country_list=[]
index_counter=0

def listCSVFiles(dir_name):
    global csv_list
    for file in os.listdir(dir_name):
        if file.endswith(".csv"):
            path=directory+"/"+file
            csv_list.append(path)
    return sorted(csv_list)

#listCSVFiles returns a list with all the csv file paths
#then we can read each one of them
#and further proscess them

def preProscessData():
    global country_list
    files=listCSVFiles(directory)
    for f in files:
        with open(f) as csvfile:
            csv_reader = csv.reader(csvfile)
            row=[r for r in csv_reader]          	#row contains all the rows of csv file with every row as a list(row[index])
            current_data=[]											 	#current_data holds the data we need for each country(years,and indicators)
            for i in range(6,len(row)):         	#after 5 rows we have all we need
                for j in range(len(indicator_list)):  #iterate through the indicator list and if we find the indicator we store the row
                    if(row[i][2]==indicator_list[j]):
                        current_data.append(row[i])      #the row that contains the indicator also contains country name,country code,indicator name,
                                                                                            #indicator code and all the elements(numbers,statistics) for the indicator
            years=row[4]


            for i in range(4): #just poping the first 4 elemnts(we dont want them)
                years.pop(0)

            current_data.append(years)
        countries_data.append(current_data)
    return countries_data

def create_dir(directory_path):

	tmp_path=directory_path.split("/")
	tmp_path.pop(len(tmp_path)-1)
	tmp_path.insert(len(tmp_path),"final_csv")
	new_path=""
	for i in range(len(tmp_path)):
		new_path=new_path+tmp_path[i]+"/"
		
	try:
		os.mkdir(new_path)
	except OSError:
		print ("Creation of the directory failed")
		
	return new_path

final_csv_path=create_dir(directory)
	
def make_csv_headers(header1,header2,*args):
    header_list=[]
    header_list.append(header1)
    header_list.append(header2)
    for i in range(len(args)):
        header_list.append(args[i])
	
    return header_list

   
def final_country_csv(path_name):
    data=preProscessData()
    sort_list=[]
    headers=make_csv_headers("Country Code","Country Name")
    path=path_name+"Country_csv.csv"
    with open(path, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(headers)
        for i in range(len(data)):
            data_list=data[i]
            country_name=data_list[0][0]
            country_code=data_list[0][1]
            if(country_name=="Egypt, Arab Rep."):
                country_name=country_name.split(",")[0]+country_name.split(",")[1]
            sort_list.append((country_code,country_name))
        sort_list=sorted(sort_list,key=lambda x: x[0])
        id=0
        for i in range(len(sort_list)):
            tup=(sort_list[i][0],sort_list[i][1])
            filewriter.writerow(tup)
    return 

def final_indicator_csv(path_name):
    data=preProscessData()
    headers=make_csv_headers("Indicator Code","Indicator Name","Measurement unit")
    path=path_name+"Indicator_csv.csv"
    with open(path, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(headers)
        for i in range(len(data)):
            data_list=data[i]
            if(len(data_list)==13):
                for j in range(len(data_list)-1):
                    current_data=data_list[j]
                    raw_indicator_name=current_data[2]
                    mes_unit_list=re.split(r'[\(\)]',raw_indicator_name)
                    actual_indicator_name=mes_unit_list[0]
                    actual_mes_unit=mes_unit_list[1]
                    if("," in actual_indicator_name):
                        indicator_name=actual_indicator_name.split(",")
                        actual_indicator_name=indicator_name[0]+""+indicator_name[1]
                    indicator_code=current_data[3]
                    filewriter.writerow([indicator_code,actual_indicator_name, actual_mes_unit])
                break
    return

def final_data_csv(path_name):
    data=preProscessData()
    values=[]
    headers=make_csv_headers("id","Country Code","Indicator Code","Year","Indicator Value")
    path=path_name+"Data_csv.csv"
    with open(path, 'w') as csvfile:
        id=0
        filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(headers)
        for i in range(len(data)-1):
            data_list=data[i]
            years= data_list[len(data_list)-1]
            for k in range(len(data_list)-1):
                current_data=data_list[k]
                country_code=current_data[1]
                indicator_code=current_data[3]
                for j in range(len(years)-1):
                    current_year=years[j]
                    id=id+1
                    current_value=current_data[j+4]
                    if(current_value=="" ):
                        current_value=-1
                    filewriter.writerow([id,country_code,indicator_code,current_year,current_value])
            if(data_list[0][1]=="TUN"):
                break
    return
	

def final_group_years_csv(path_name):
    data=preProscessData()
    headers=make_csv_headers("Year","5 Years","10 Years")
    path=path_name+"Year_Group_csv.csv"
    with open(path, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(headers)
        for i in range(len(data)):
            data_list=data[i]
            years= data_list[len(data_list)-1]
            break
        for j in range(len(years)-1):
            current_year=years[j]
            if(current_year>=str(1960) and current_year<=str(1969)):
                if(current_year<=str(1964)):
                    filewriter.writerow([years[j],"1960-1964","1960-1969"])
                else:
                    filewriter.writerow([years[j],"1965-1969","1960-1969"])
            elif(current_year>=str(1970) and current_year<=str(1979)):
                if(current_year<=str(1974)):
                    filewriter.writerow([years[j],"1970-1974","1970-1979"])
                else:
                    filewriter.writerow([years[j],"1975-1979","1970-1979"])
            elif(current_year>=str(1980) and current_year<=str(1989)):
                if(current_year<=str(1984)):
                    filewriter.writerow([years[j],"1980-1984","1980-1989"])
                else:
                    filewriter.writerow([years[j],"1985-1989","1980-1989"])
            elif(current_year>=str(1990) and current_year<=str(1999)):
                if(current_year<=str(1994)):
                    filewriter.writerow([years[j],"1990-1994","1990-1999"])
                else:
                    filewriter.writerow([years[j],"1995-1999","1990-1999"])
            elif(current_year>=str(2000) and current_year<=str(2009)):
                if(current_year<=str(2004)):
                    filewriter.writerow([years[j],"2000-2004","2000-2009"])
                else:
                    filewriter.writerow([years[j],"2005-2009","2000-2009"])
            elif(current_year>=str(2010) and current_year<=str(2019)):
                if(current_year<=str(2014)):
                    filewriter.writerow([years[j],"2010-2014","2010-2019"])
                else:
                    filewriter.writerow([years[j],"2015-2019","2010-2019"])
            else:
                return
            
            
            
            

def export_normalized_csv():
    print("Exporting normalized csv's ...")
    final_country_csv(final_csv_path)
    final_indicator_csv(final_csv_path)
    final_data_csv(final_csv_path)
    final_group_years_csv(final_csv_path)
    time.sleep(2)
    print("Finished")
    return


export_normalized_csv()

