import re
import sys
import csv
import pymysql

global cursor

dir = "/home/bilbo/Desktop/python/project--/final_csv"

def csv_to_mysql():
    global cursor
    try: 
        connection = create_connection()
        #create cursor
        cursor = connection.cursor()
        cursor.execute("USE mydb;")
        #load each table
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0;") #gia na mhn xtypane ta ksena kleidia ypotithetai oti prepei prwta na gemiseis pinakes kai meta na baleis me alter table ta ksena kleidia. me ayto to set 0 kai meta 1 glytwnoyme ayto
        load_Countries()
        load_Years()
        load_Indicators()
        load_Data()
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
        connection.close()
    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)

def create_connection():
    con = pymysql.connect(host= 'localhost', user = 'root', password = '2512271997bass',autocommit=True, local_infile=1)
    print("Connect to database: {}".format('127.0.0.1'))
    return con

def load_Countries():
    table_name = "Countries"
    create_table = "CREATE TABLE IF NOT EXISTS Countries (countryCode VARCHAR(3) NOT NULL UNIQUE, countryName VARCHAR(45) NOT NULL UNIQUE, PRIMARY KEY (countryCode)) ENGINE = InnoDB"
    load_query = """LOAD DATA INFILE "/home/bilbo/Desktop/python/project--/final_csv/Country_csv.csv" INTO TABLE Countries FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES;"""
    execute_query(load_query, create_table, table_name)


def execute_query(load_query, create_table, table_name):
    global cursor
    cursor.execute(create_table)
    cursor.execute(load_query) #load table command
    print('Successfully loaded the table {}'.format(table_name))

def load_Years():   
    table_name = "Years" 
    create_table = "CREATE TABLE IF NOT EXISTS Years (year INT(11) NOT NULL UNIQUE, 5yearPeriod VARCHAR(11) NOT NULL, 10yearPeriod VARCHAR(11) NOT NULL, PRIMARY KEY (year)) ENGINE = InnoDB"
    load_query = """LOAD DATA INFILE "/home/bilbo/Desktop/python/project--/final_csv/Year_Group_csv.csv" INTO TABLE Years FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES;"""
    execute_query(load_query, create_table, table_name)

def load_Indicators():  
    table_name = "Indicators"
    create_table = "CREATE TABLE IF NOT EXISTS Indicators (indicatorCode VARCHAR(20) NOT NULL UNIQUE, indicatorName VARCHAR(100) NOT NULL UNIQUE, measurementUnit VARCHAR(45) NOT NULL, PRIMARY KEY (indicatorCode)) ENGINE = InnoDB"
    load_query = """LOAD DATA INFILE "/home/bilbo/Desktop/python/project--/final_csv/Indicator_csv.csv" INTO TABLE Indicators FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES;"""
    execute_query(load_query, create_table, table_name)

def load_Data():    
    table_name = "Data"
    create_table = "CREATE TABLE IF NOT EXISTS Data (id INT(11) NOT NULL UNIQUE, countryCode VARCHAR(3) NOT NULL, indicatorCode VARCHAR(20), year INT(11) NOT NULL, value DECIMAL(40,20), PRIMARY KEY (id),FOREIGN KEY (countryCode) REFERENCES Countries(countryCode) ON DELETE CASCADE ON UPDATE CASCADE, FOREIGN KEY (indicatorCode) REFERENCES Indicators(indicatorCode) ON DELETE CASCADE ON UPDATE CASCADE, FOREIGN KEY (year) REFERENCES Years(year) ON DELETE CASCADE ON UPDATE CASCADE) ENGINE = InnoDB"
    load_query = """LOAD DATA INFILE "/home/bilbo/Desktop/python/project--/final_csv/Data_csv.csv" INTO TABLE Data FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES;"""
    execute_query(load_query, create_table, table_name)

csv_to_mysql()