import os,json
from flask import Flask
from flask_restful import Api,Resource
from server.api import UserAPI,MachineAPI,ParkingAPI
from server.models import User,Machine,Parking
from flask_mqtt import Mqtt
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()

# settings
app=Flask(__name__)
app.secret_key=os.urandom(16).hex()
app.config['MQTT_BROKER_URL'] = 'mqtt.ckcsc.net'
app.config['MQTT_BROKER_PORT'] = 5900
app.config['MQTT_USERNAME'] = os.environ['MQTT_USER']
app.config['MQTT_PASSWORD'] = os.environ['MQTT_PASS']
# app.config['MQTT_KEEPALIVE'] = 5
app.config['MQTT_TLS_ENABLED'] = False

api = Api(app)
mqtt = Mqtt(app)
CORS(app,resources={r"/api/*": {"origins": "*"}}) # enable cross origin resource sharing policy

# setup for restful API interface
api.add_resource(UserAPI,'/api/user')
api.add_resource(ParkingAPI,'/api/parking')
api.add_resource(MachineAPI,'/api/machine')

# mqtt
@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('RoadParking/+')

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    print(data['payload'])
    
    if data['topic']=='RoadParking/Machine':# update for each machine status
        #status
        #ip
        #other information
        json_data=json.loads(data['payload'])
        # json_data [key_value, data]
        Machine.edit_machine(json_data[0],json_data[1])
        pass
    elif data['topic']=='RoadParking/Parking':# update for each parking space
        pass

if __name__=='__main__':
    app.run(port=8000)