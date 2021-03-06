***********************************************************
## ECEN 5783 Embedded Interface Design Assignment 4

### Team: Antara Prakash and Nitik Gupta

### Special Instructions: 

* To run the app.js for sensor simulation, use node app.js {Number of sensors}
* If there is no database in your MySQL, app.js will create it for you.
* Use python3 to execute the python programs
* to exit programs, use ctrl+c
* to open the html file, double-click the index.html file.
* If the servers were not already opened, then there wont be any successful connection, so need to open the servers first, then the HTML Client.
* Whoever executes this codes, need to have Tornado,chart.js, and multiple dependencies installed already, else it might give some errors.

### Language Used : Python and JavaScript(compiled using node.js)

### Program Design

There are two servers:
1. Tornado Server: A python program implementing the Tornado Webserver to connect to the MySQL database.
2. node.js Server: A javascript based 
We assumed that there is a 5% chance of getting a -3 to -8 value difference, and 5% chance of getting a 3 to 9 value difference. cumulatively getting a 10% chance of upto 8 degree difference

### Assumptions

The Threshold value wont be changed in the sensor program, so the alarms wont be written in sensor or in the mysql database.
The threshold by default is 45, now if you change the threshold value from tab 3, it will raise the alarm from starting in TouchScreen UI.
It wont still write to the MySQL Database.
Python is not creating the matplotlib images, instead the HTML client is using the chart.js for plotting the data points.

### Files included:

#### sensor.js: 
This file contains the program for a sensor that will record the temperature, timestamp, alarms, errors, sensor number to a json file.
#### app.js: 
This File contains the application part of the sensor, to insert an query, to create a table
#### db.js: 
This file has database for the project
#### TouchScreen.py:
This program takes all the values from mysql database and displas the temperature variation on graph
#### TouchScreen_Helper.py: 
A Helper file for touchscreen UI
#### index.html: 
The HTML Client for database to display data and plot the temperature points for each sensor vs the time stamp.
#### server.js: 
The javascript file that interconncts the database and the node to the HTML client.
#### tornado_server.py
The Python script that executes the Tornado Webserver to send the data to the HTML client taken from the master.py file.
### EID Project Proposal.pdf
PDF file that describes the super project of the course.

**********************************************************