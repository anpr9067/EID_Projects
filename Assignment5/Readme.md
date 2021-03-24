***********************************************************
## ECEN 5783 Embedded Interface Design Assignment 5

### Team: Antara Prakash and Nitik Gupta

### Special Instructions: 

* Use python3 to execute the python programs
* to exit programs, use ctrl+c
* to open the html file, double-click the index.html file.
* If the servers were not already opened, then there wont be any successful connection, so need to open the servers first, then the HTML Client.
* Whoever executes this codes, need to have zeromq, AWS Iot thing and multiple dependencies installed already, else it might give some errors.

### Language Used : Python

### Program Design

There are two servers:
1. ZeroMQ Server: A python program implementing the ZeroMQ Webserver to connect to send data.
We assumed that there is a 5% chance of getting a -3 to -8 value difference, and 5% chance of getting a 3 to 9 value difference. cumulatively getting a 10% chance of upto 8 degree difference

### Assumptions

The Threshold value wont be changed in the sensor program, so the alarms wont be written in sensor or in the mysql database.
The threshold by default is 45, now if you change the threshold value from tab 3, it will raise the alarm from starting in TouchScreen UI.
It wont still write to the MySQL Database.
Python is not creating the matplotlib images, instead the HTML client is using the chart.js for plotting the data points.

### Files included:

#### Client.py
This file contains the functions to connect to the server file, 
 						and calculate the data and send the data to server.
This file contains the program for a sensor that will record the temperature, timestamp, alarms, errors, sensor number to a json file.
#### server.py 
This file contains the functions to connect to client file,and get the json data from there and send the data to AWS IoT ThingA.
#### WBS_Antara_Nitik.png: 
Work Breakdown Structure for this project
#### .crt or .key or root-ca.pem 
Files for the certificates and keys for AWS IoT thing.

**********************************************************