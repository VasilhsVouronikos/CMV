import sys,os
import mysql.connector

global cursor,conn
sql_output = []
formated_input = []
input_Countries = []
input_Indicators = []
input_Year = ""
input_period = ""

given_Countries = [
	"Greece","Brazil","Canada",
	"Switzerland","Germany",
	"Kenya","Japan","Russia",
	"Egypt","Tunisia","India"
]
given_Indicators = [
	"Merchandise imports by the reporting economy","Gross domestic savings",
	"Total natural resources rents","GDP per capita growth",
	"Energy imports net","Exports as a capacity to import",
	"Trade","Gross capital formation","Gross domestic savings",
	"Exports of goods and services","GDP deflator"
]


class Connector:

	def __init__(self):
		with open(os.getcwd()+"/credentials.txt","r") as credit:
			res = []
			for lines in credit:
				line = lines.strip("\n").split("=")
				res.append(line[1])
			
			self.user = res[0]
			self.password = res[1]
			self.host = res[2]
			self.db_name = res[3]
		return

	def connect(self):
		global cursor,conn
		conn = mysql.connector.connect(user = self.user, password = self.password,host = self.host,database = self.db_name)
		print("Connection to database established: {}".format('127.0.0.1'))
		try:
			cursor = conn.cursor()
		except Exception as e:
			print('Error: {}'.format(str(e)))
			sys.exit(1)

	def excecute_query(self,data):
		global cursor,formated_input,sql_output

		del sql_output[:]       # if something is in due to previous querie delete it
		del formated_input[:]   # also delete previous input from client
		del input_Indicators[:]
		del input_Countries[:]

		for i in range(len(data)):
			replaced_string = data[i].replace('"', "")  #formating strings from '"string"' to 'string'
			formated_input.append(replaced_string)


		for i in range(len(formated_input)):
			if(formated_input[i] in given_Countries):
				input_Countries.append(formated_input[i]+"\r")
			if(formated_input[i] in given_Indicators):
				input_Indicators.append(formated_input[i])


		input_Year = formated_input[len(formated_input) -3]
		input_period = formated_input[len(formated_input) -2]
		input_plot = formated_input[len(formated_input) -1]

		country_list = tuple(input_Countries)
		indicator_list = tuple(input_Indicators)

		
		output = self.queries_from_indicators(indicator_list,country_list,input_Year,input_period,input_plot)

		

		return output

	def queries_from_countries(self,countryL):
		global cursor
		result = []
		countryCode = []

		try:
			for name in countryL:
				sql = """SELECT countryCode FROM Countries WHERE countryName = %s"""
				cursor.execute(sql,(name,))
				for i in cursor: 
					result.extend(i)

		except mysql.connector.Error as e:
			return "no result"

		return tuple(result)


	# questionds based on indicators
	def queries_from_indicators (self,indicatorL,countryL,year,period,plot):
		global cursor,conn
		result = []
		indicatorCode=[]
		countryCode = self.queries_from_countries(countryL)
		years = self.get_years(period,year)
		try:
			for ind in indicatorL:
				
				sql = """SELECT indicatorCode FROM Indicators WHERE IndicatorName = %s""" 
				cursor.execute(sql,(ind,))
				for i in cursor:
					indicatorCode.extend(i)

				
		except mysql.connector.Error as e:
			print(e)
			return "no result"

		if(year == "All" and (plot == "line" or plot == "bar")):

			try:
				for name in countryCode:
					for ind in indicatorCode:
					
						sql = """SELECT year,value FROM Data WHERE IndicatorCode = %s and countryCode = %s"""
						cursor.execute(sql,(ind,name,))
						for i in cursor:
							result.append(i)
						print(result)
			except mysql.connector.Error as e:
				print(e)
				return "no result"

		elif(year == "All" and plot == "scatter"):

			try:
				for name in countryCode:
					for ind in indicatorCode:
						sql = "SELECT year,value FROM Data WHERE IndicatorCode = %s and countryCode = %s"
						for i in cursor:
							result.append(i)
			except mysql.connector.Error as e:
				return "no result"

		elif(year != "All" and (plot == "line" or plot == "bar")):
			year_tuple = years[0]
			if(year_tuple == year):
				first_year = years[0]
				last_year = years[0]
			else:
				 #year_tuple = years[0]
				year_range = year_tuple[0].split("-")
				first_year = year_range[0]
				last_year = year_range[1]
			try:
				for name in countryCode:
					for ind in indicatorCode:
						sql = """SELECT year,value FROM Data WHERE IndicatorCode = %s and countryCode = %s and Year >= %s and Year <= %s"""
						cursor.execute(sql,(ind,name,first_year,last_year,))
						for i in cursor:
							result.append(i)
			except mysql.connector.Error as e:
				return "no result"

		elif(year != "All" and plot == "scatter"):
			year_tuple = years[0]
			if(year_tuple == year):
				first_year = years[0]
				last_year = years[0]
			else:
				
				year_range = year_tuple[0].split("-")
				first_year = year_range[0]
				last_year = year_range[1]

			try:
				for name in countryCode:
					for ind in indicatorCode:
						sql = """SELECT year,value FROM Data WHERE IndicatorCode = %s and countryCode = %s and Year >= %s and Year <= %s"""
						cursor.execute(sql,(ind,name,first_year,last_year,))
						for i in cursor:
							result.append(i)
			except mysql.connector.Error as e:
				return "no result"
		else:
			result = "No data"

		return result
			
	def get_years(self,period,year):
		global cursor
		if(year == "All"):
			return "all"
		else:
			years = []
			try:
				if(period == str(5)):
					sql = """SELECT 5yearPeriod FROM Years WHERE year = %s""" 
					cursor.execute(sql,(year,))
					for i in cursor:
						years.append(i)
				if(period == str(10)):
					sql = """SELECT 10yearPeriod FROM Years WHERE year = %s""" 
					cursor.execute(sql,(year,))
					for i in cursor:
						years.append(i)
				if(period == str(1)):
					years.append(year)	
			except mysql.connector.Error as e:
				print(e)
				return "no result"
		
		return years


		

