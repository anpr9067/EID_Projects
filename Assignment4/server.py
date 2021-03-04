	# https://stackoverflow.com/questions/43796423/python-converting-mysql-query-result-to-json
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import mysql.connector
import json
from Graphical_Representation import Update_Fun
from datetime import datetime
import itertools
import matplotlib.pyplot as plt
from flask import jsonify
'''
This is a simple Websocket Echo server that uses the Tornado websocket handler.
Please run `pip install tornado` with python of version 2.7.9 or greater to install tornado.
This program will echo back the reverse of whatever it recieves.
Messages are output to the terminal for debuggin purposes. 
''' 
 
class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print ('new connection')
      
    def on_message(self, message):
        # Connecting to MySQL Database
        cnx = mysql.connector.connect(host = 'localhost',user='root', database='eid',password='password')
        cursor = cnx.cursor()
        # Get number of sensors
        sensorid=int(message)
        sensor_num = 6
        buffer = "SELECT * FROM eid.sensor where sensornumber="+str(sensorid)+" ORDER BY id DESC LIMIT 10;"
        cursor.execute(buffer)
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        rv = cursor.fetchall()
        data2 = []
        content = {}
        for result in rv:
            content = {'id': result[0], 'TimeStamp':result[1], 'sensornumber':result[2],"Tempreture":result[3],"Humidity":result[4],"Alarm_Count_Temp":result[5],"Alarm_Count_Hum":result[6],"Error_Count":result[7]}
            data2.append(content)
        data1 = json.dumps(data2)
        data = [[]]*(sensor_num*2)
        flag = [0]*(sensor_num*2)
        base_seconds = 0;
        buffer = "SELECT * FROM eid.sensor where sensornumber="+str(sensorid)+" ORDER BY id LIMIT 10;"
        cursor.execute(buffer)
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
        # Plotting all the curves
        plt.clf()
        plt.plot(data[2*sensorid+1],data[2*sensorid])
        # Plotting all the curves
        plt.xlabel('Time(in seconds)')
        plt.ylabel('Temperature(in Fahrenheit)')
        plt.title('Temperature variations by sensor' + str(sensorid))
        plt.savefig('Plot.png')
        self.write_message(data1)
        # print(data)
        # Reverse Message and send it back
        # print ('sending back message: %s' % temp_data[1][-1])
        # self.write_message(json.dumps(temp_data))
 
    def on_close(self):
        print ('connection closed')
 
    def check_origin(self, origin):
        return True

application = tornado.web.Application([
    (r'/', WSHandler),
])
 
 
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    myIP = socket.gethostbyname(socket.gethostname())
    print ('*** Websocket Server Started at %s***' % myIP)
    tornado.ioloop.IOLoop.instance().start()