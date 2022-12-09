# 發布者（publisher）指令稿 publisher1.py
import paho.mqtt.client as mqtt
import ssl
# 建立 MQTT Client 物件
client = mqtt.Client()



def hello(a,b,c):
    print(1)
client.on_publish=hello

# 設定登入帳號密碼（若無則可省略）
client.username_pw_set("timothy","123123123")
client.connect("mqtt.ckcsc.net", 5900,60)
# 發布訊息至 hello/world 主題
# client.loop_start()
client.publish("RoadParking/Parking", 'Timothychen',qos=2,retain=False)
client.loop_forever()
print(1)