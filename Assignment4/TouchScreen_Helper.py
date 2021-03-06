#	FileName: TouchScreen_Helper.py
#	File Description: This program takes all the values from mysql database and sends to the touchsceen function for Adjustment
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


def Update_Function():
	# Connecting to MySQL Database
	cnx = mysql.connector.connect(host = 'localhost',user='root', database='eid',password='password')
	cursor = cnx.cursor()
	# Executing the MySQL commands
	buffer = "USE eid"
	cursor.execute(buffer)
	sensor_num = 6
	global temp_data,hum_data,number_of_rows,Last_ID
	# Get number of rows
	cursor.execute("SELECT count(*) FROM eid.sensor")
	number_of_rows = cursor.fetchone()[0]
	number_of_rows = int(number_of_rows)
	buffer = "SELECT * FROM eid.sensor;"
	cursor.execute(buffer)
	# List to store data
	temp_data = [[]]*(sensor_num*5)
	hum_data = [[]]*(sensor_num*5)
	flag = [0]*(sensor_num*5)
	TempAlarm = [0]*(sensor_num)
	HumAlarm = [0]*(sensor_num)
	Last_ID = [1]*(2*sensor_num)
	base_seconds = 0;
	for (ID,TIME,SENSOR,TEMP,HUM,ALARM1, ALARM2,ERROR) in cursor:
		# Converting to base number of seconds
		TimeStamp = datetime.strptime(TIME, "%m/%d/%Y, %H:%M:%S %p")
		seconds = int(TimeStamp.timestamp())
		if(base_seconds == 0):
			base_seconds = int(TimeStamp.timestamp())
		seconds = seconds - base_seconds
		if flag[5*SENSOR] == 0:
			if(TEMP!=999):
				temp_data[5*SENSOR] = [ID]
				temp_data[5*SENSOR+1] = [TEMP]
				temp_data[5*SENSOR+2] = [ERROR]
				temp_data[5*SENSOR+3] = [ALARM1]
				temp_data[5*SENSOR+4] = [seconds]
				flag[5*SENSOR] = 1
			if(HUM!=999):
				hum_data[5*SENSOR] = [ID]
				hum_data[5*SENSOR+1]= [HUM]
				hum_data[5*SENSOR+2] = [ERROR]
				hum_data[5*SENSOR+3] = [ALARM2]
				hum_data[5*SENSOR+4] = [seconds]
				flag[5*SENSOR] = 1
		elif flag[5*SENSOR] == 1:
			if(TEMP!=999):
				from TouchScreen import Temp_Thres
				if(TEMP >= Temp_Thres):
					TempAlarm[SENSOR]+=1
				temp_data[5*SENSOR].append(ID)
				temp_data[5*SENSOR+1].append(TEMP)
				temp_data[5*SENSOR+2].append(ERROR)
				temp_data[5*SENSOR+3].append(TempAlarm[SENSOR])
				temp_data[5*SENSOR+4].append(seconds)
				Last_ID[2*SENSOR] = ID
			if(HUM!=999):
				from TouchScreen import Hum_Thres
				if(HUM >= Hum_Thres):
					HumAlarm[SENSOR]+=1
				hum_data[5*SENSOR].append(ID)
				hum_data[5*SENSOR+1].append(HUM)
				hum_data[5*SENSOR+2].append(ERROR)
				hum_data[5*SENSOR+3].append(HumAlarm[SENSOR])
				hum_data[5*SENSOR+4].append(seconds)
				Last_ID[2*SENSOR+1] = ID
	# print(temp_data)
	cursor.close()
	cnx.close()
		
Update_Function()