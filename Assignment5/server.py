#	FileName: server.py
#	File Description: This file contains the functions to connect to client file, 
# 						and get the json data from there and send the data to AWS IoT ThingA.
# 	Resources: https://aws.amazon.com/premiumsupport/knowledge-center/iot-core-publish-mqtt-messages-python/
# 				Some of the things from previous assignments from the same subject.
import time
#from temp import sensor_param
import json
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import zmq

RANGE = 300
i = 0
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
myMQTTClient = AWSIoTMQTTClient("myClientID")
myMQTTClient.configureEndpoint("a37k9ro04gprkh-ats.iot.us-east-1.amazonaws.com", 8883)
myMQTTClient.configureCredentials("root-ca.pem", "9670267452-private.pem.key", "9670267452-certificate.pem.crt")
# For Websocket, we only need to configure the root CA
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
TOPIC = "SensorEIDPolicy"
myMQTTClient.connect()
for i in range (RANGE):
    mes = socket.recv()
    message = json.loads(mes.decode('utf-8'))
    print("Received request:",message)
    myMQTTClient.publish(TOPIC, json.dumps(message), 1) 
    print("Published: '" + json.dumps(message) + "' to the topic: " + "'test/testing'")
    time.sleep(1)
    socket.send(b"Success")
print('Publish End')
myMQTTClient.disconnect()
    