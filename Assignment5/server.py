# Import SDK packages
import time
from temp import sensor_param
import json
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import zmq

RANGE = 300
i = 0
# data1 = {
#     "message": "hii from pyton ..."
# }

# def myfunc(x):
#     data = sensor_param(x)
#     return data

# For certificate based connection
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
myMQTTClient = AWSIoTMQTTClient("myClientID")
# For Websocket connection
# myMQTTClient = AWSIoTMQTTClient("myClientID", useWebsocket=True)
# Configurations
# For TLS mutual authentication
myMQTTClient.configureEndpoint("a37k9ro04gprkh-ats.iot.us-east-1.amazonaws.com", 8883)
# For Websocket
# myMQTTClient.configureEndpoint("YOUR.ENDPOINT", 443)
# For TLS mutual authentication with TLS ALPN extension
# myMQTTClient.configureEndpoint("YOUR.ENDPOINT", 443)
myMQTTClient.configureCredentials("root-ca.pem", "9670267452-private.pem.key", "9670267452-certificate.pem.crt")
# For Websocket, we only need to configure the root CA
# myMQTTClient.configureCredentials("YOUR/ROOT/CA/PATH")
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
# while True:
#     data0 = myfunc(0);
#     time.sleep(1)
#     data1 = myfunc(1);
#     time.sleep(1)
#     data2 = myfunc(2);
    
#     print("Connected ... ")
#     # data1 = {
#     #     "message": i
#     # }
#     myMQTTClient.publish("SensorEIDPolicy", json.dumps(data0) , 0)
#     myMQTTClient.publish("SensorEIDPolicy", json.dumps(data1) , 0)
#     myMQTTClient.publish("SensorEIDPolicy", json.dumps(data2) , 0)
#     # myMQTTClient.subscribe("myTopic", 1, customCallback)
#     # myMQTTClient.unsubscribe("myTopic")
#     #i = i+1
#     time.sleep(8)
print('Publish End')
myMQTTClient.disconnect()
    