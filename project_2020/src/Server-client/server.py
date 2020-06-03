from flask import Flask,render_template,url_for,jsonify,request
import sys,os
import re
from db_connect import Connector


app = Flask(__name__)

global cursor,db_connection
js_incoming_data = []
test_string = ""


@app.route('/')
def home():
	return render_template('home.html')  #route for home page

@app.route('/queries')
def queries():
	
	return render_template('queries.html')  #route for queries page


@app.route('/get_rec', methods = ['POST'])  # route for communication between server and client
def get_post_javascript_data():
	global js_incoming_data,test_string

	jsdata = request.form['jsdata']

	if(jsdata == "hello from web page"):  # if we just testing withoun selecting something from web page
		print(jsdata)					  # client will send that string
		test_string = "hello from flask"  # and we will send back test_string
		data_to_js = test_string
	else:
		data_to_js = proscess_data(jsdata)  # else we will oparate normally by excecuting queries

	
	return jsonify({"response" : data_to_js}) # when it comes to test communication replace data_to_js with test string here

# proscess client incoming data
def proscess_data(data):
	global js_incoming_data

	prosc_data = re.findall("\[([^[\]]*)\]", data)
	tmp_list = []

	for i in range(len(prosc_data)):
		
		tmp_list.append(re.findall('"[^"]+"', prosc_data[i]))  # remove '[]' chars from incoming json

	# after gathering the data we are ready to excecute a query

	for i in range(len(tmp_list)):
		for j in range(len(tmp_list[i])):
			js_incoming_data.append(tmp_list[i][j])


	output = db_connection.excecute_query(js_incoming_data)
	with open(os.getcwd()+"/queries_output.txt","w+") as f:
		for i in output:
			f.write(str(i))
			f.write("\n")

	del js_incoming_data [:]

	return output

def start_server():
	connect_db()
	app.run(debug=True, host='0.0.0.0')

def connect_db():
	global db_connection
	db_connection = Connector()    #Class Connector from db_connector file

	conn = db_connection.connect()  #connection to database

start_server()  				   
