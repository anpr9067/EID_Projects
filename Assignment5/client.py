#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq
import json
import random
import time 
from datetime import datetime

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
request=0
base = 40
alarm=0
error=0
#  Do 10 requests, waiting each time for a response
while True:

	for sense in range(1,4):
		r = random.randint(1,100)	# random number to get the probability
		if(r>=91 and r<=95):		# 5% chance for -3 to -8
			t = base + random.randint(-8,-3)
		elif(r>=95 and r<=100):		# 5% chance for 3 to 8
			t = base + random.randint(3,8)
			if( t >= base + 5 ):
				alarm+=1
		elif(r>=81 and r<=90):		# 10% chance for error number
			t = 999
			error+=1
		else:
			t = base + random.randint(-2,2)
		r = random.randint(1,100)	# random number to get the probability
		if(r>=91 and r<=95):		# 5% chance for -3 to -8
			h = base + random.randint(-8,-3)
		elif(r>=95 and r<=100):		# 5% chance for 3 to 8
			h = base + random.randint(3,8)
			if( h >= base + 5 ):
				alarm+=1
		elif(r>=81 and r<=90):		# 10% chance for error number
			h = 999
			error+=1
		else:
			h = base + random.randint(-2,2)
		now = datetime.now()	# getting the current time stamp
		timestamp = datetime.timestamp(now)
		dt = datetime.fromtimestamp(timestamp)	# chaning to better format
		dt_object = json.dumps(dt,default = str)
		record = {
				"Sensor":sense,
				"Time":dt_object,
				"Temp":t,
				"Humidity":h,
				"Alarm_Temperature_level":base,
				"Alarm_Humidity_level":base,
				"Alarm":alarm,
				"Error":error
				}
		print("Sending request : ",record)
		socket.send_json(record)
		request+=1
		#  Get the reply.
		message = socket.recv()
		print("Received reply : ",message)
		time.sleep(1)