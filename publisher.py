from dotenv import load_dotenv
import os
load_dotenv()

import paho.mqtt.publish as publish

payload ={''}

auth = {'username': "timothy", 'password': os.environ['MQTT_PASS']}


publish.single('RoadParking/Machine', payload, qos=2, hostname='mqtt.ckcsc.net',port=5900,auth=auth)
