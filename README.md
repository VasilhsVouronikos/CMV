# Project_2020_MYE030-PLYE045
CREATORS:
Ioanna Kougia
Padelhs Mhtshs
Vasilis Vouronikos


DESCRIPTION:

In this project we have created a web app that visualizes the 
relationship between metrics of different countries.We chose
12 metrics,12 countries in te range of years between 1960 and 2019.
All countries and metrics information can be found in the initial
page of our web app.

INSTALATION:

------PYTHON MODULES------------
In the env_setup folder you will find setup.py script,
run it to automaticaly install the required python modules.
If this dont work install the following modules by hand
install python Flask (command: pip3 install Flask),
install python jsonify (command: pip3 install jsonify),
install python request (command: pip3 install request),
install python pymysql (command: pip3 install pip mysql-connector-python)

------MySQL----------
install MySQL-server
install MySQL workbench

------Javascript-------
install javascript.

RUNNING:

Firstly create a database with the name mydb and then
load the database tables through backup files located in database_buckup folder into workbech.
When the database is ready open credentials.txt located in Server-client folder
and change your database credentials accordingly.So now everything
is almost done,start the server by running server.py and open a 
browser in the url 0.0.0.0/5000 and you are ready to go.


DISPLAY DATABASE OUTPUT:

The ouput of every query will be written
in queries.txt show the user can see the 
database output for every avaliable question
