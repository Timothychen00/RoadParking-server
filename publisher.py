# 發布者（publisher）指令稿 publisher1.py
import paho.mqtt.client as mqtt
import ssl
from dotenv import load_dotenv
import os
load_dotenv()
# 建立 MQTT Client 物件
client = mqtt.Client('hello')



def hello(a,b,c):
    print(1)
client.on_publish=hello

# 設定登入帳號密碼（若無則可省略）
client.username_pw_set("timothy",os.environ['MQTT_PASS'])
client.connect("mqtt.ckcsc.net", 5900,60)
# 發布訊息至 hello/world 主題
# client.loop_start()
client.publish("RoadParking/Machine", '{"type":"esp8266"}',qos=2,retain=False)
client.loop_forever()
print(1)