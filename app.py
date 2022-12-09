import os
from flask import Flask
from server.routes import app_route
from flask_restful import Api,Resource
from server.api import UserAPI,MachineAPI,ParkingAPI
from flask_mqtt import Mqtt
from dotenv import load_dotenv
load_dotenv()

app=Flask(__name__)

app.secret_key=os.urandom(16).hex()
app.config['MQTT_BROKER_URL'] = 'mqtt.ckcsc.net'
app.config['MQTT_BROKER_PORT'] = 5900
app.config['MQTT_USERNAME'] = ''
app.config['MQTT_PASSWORD'] = ''
app.config['MQTT_KEEPALIVE'] = 5
app.config['MQTT_TLS_ENABLED'] = False

api = Api(app)
mqtt = Mqtt(app)
app.register_blueprint(app_route)

# setup for restful API interface
api.add_resource(UserAPI,'/api/user')
api.add_resource(ParkingAPI,'/api/parking')
api.add_resource(MachineAPI,'/api/machine')

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

if __name__=='__main__':
    app.run(debug=True,port=5000)