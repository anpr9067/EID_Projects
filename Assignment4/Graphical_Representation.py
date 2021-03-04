#	FileName: Graphical_Representation.py
#	File Description: This program takes all the values from mysql database and displas the temperature variation on graph
#	Author: Nitik Gupta
#	References: https://realpython.com/python-matplotlib-guide/
#				https://www.geeksforgeeks.org/python-list/
#				https://python-graph-gallery.com/122-multiple-lines-chart/
#				https://www.w3resource.com/graphics/matplotlib/basic/matplotlib-basic-exercise-5.php
#				https://stackoverflow.com/questions/13091649/unique-plot-marker-for-each-plot-in-matplotlib
from datetime import datetime
import mysql.connector
import matplotlib.pyplot as plt
import numpy as np
import itertools

# Connecting to MySQL Database
def Update_Fun():
	cnx = mysql.connector.connect(host = 'localhost',user='root', database='eid',password='password')
	cursor = cnx.cursor()

	# Executing the MySQL commands
	buffer = "USE eid"
	cursor.execute(buffer)
	# Get number of sensors
	buffer = "SELECT MAX(sensornumber) AS maximum FROM eid.sensor"
	cursor.execute(buffer)
	sensor_num = cursor.fetchone()[0]
	sensor_num = int(sensor_num) + 1
	# Get number of rows
	cursor.execute("SELECT count(*) FROM eid.sensor")
	number_of_rows = cursor.fetchone()[0]
	number_of_rows = int(number_of_rows)
	buffer = "SELECT * FROM eid.sensor;"
	cursor.execute(buffer)
	# List to store data
	data = [[]]*(sensor_num*2)
	flag = [0]*(sensor_num*2)
	base_seconds = 0;
	for (ID,TIME,SENSOR,TEMP,HUMIDITY,ALARM1,ALARM2,ERROR) in cursor:
		# Converting to base number of seconds
		TimeStamp = datetime.strptime(TIME, "%m/%d/%Y, %H:%M:%S %p")
		seconds = int(TimeStamp.timestamp())
		if(base_seconds == 0):
			base_seconds = int(TimeStamp.timestamp())
		seconds = seconds - base_seconds
		if flag[2*SENSOR] == 0:
			if (TEMP != 999):
				data[2*SENSOR]=[TEMP]
				
				data[2*SENSOR+1]= [seconds]
				flag[2*SENSOR]=1
		elif flag[2*SENSOR] == 1:
			if(TEMP!=999):
				data[2*SENSOR].append(TEMP)
				data[2*SENSOR+1].append(seconds)
	# Different markers for different plots
	marker = itertools.cycle((',', '+', '.', 'o', '*')) 
	# Plotting all the curves
	for i in range(sensor_num):
		buffer = "sensor" + str(i)
		plt.plot(data[2*i+1],data[2*i], marker = next(marker), label = buffer)
	# Plotting all the curves
	plt.xlabel('Time(in seconds)')
	plt.ylabel('Temperature(in Fahrenheit)')
	plt.title('Temperature variations by ' + str(sensor_num) +' sensors')
	plt.legend()
	plt.savefig('Plot.png',bbox_inches='None')
		
