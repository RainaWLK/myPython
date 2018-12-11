import paho.mqtt.client as paho #import the client1
import json  
import ssl
from time import sleep
import logging
logging.basicConfig(level=logging.INFO)

def on_connect(client, userdata, flags, rc):  
  global connflag
  connflag = True
  print("Connection returned result: " + str(rc) )

def on_message(client, userdata, msg):  
  print(msg.topic+" "+str(msg.payload))

def start(mqttc):
  while True:
    sleep(2)
    #if self.connect == True:
    mqttc.publish("default", json.dumps({"message": "Hello COMP680"}), qos=1)
    #else:
    #  self.logger.debug("Attempting to connect.")


mqttc = paho.Client()  
mqttc.on_connect = on_connect  
mqttc.on_message = on_message

awshost = "adw9mfri5w1h2-ats.iot.us-west-2.amazonaws.com"  
awsport = 8883  
clientId = "paho-mqtt-luke"  
thingName = "paho-mqtt-luke"  
caPath = "../cert/root-CA.crt"  
certPath = "../cert/811869d121-certificate.pem.crt"  
keyPath = "../cert/811869d121-private.pem.key"


mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)  
mqttc.connect(awshost, awsport, keepalive=60)  
mqttc.loop_start()
start(mqttc)
