import paho.mqtt.client as mqtt

# 建立連線（接收到 CONNACK）的回呼函數
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # 每次連線之後，重新設定訂閱主題
    client.subscribe("RoadParking/+")

# 接收訊息（接收到 PUBLISH）的回呼函數
def on_message(client, userdata, msg):
    print("[{}]: {}".format(msg.topic, str(msg.payload)))

# 建立 MQTT Client 物件
client = mqtt.Client()

# 設定建立連線回呼函數
client.on_connect = on_connect

# 設定接收訊息回呼函數
client.on_message = on_message

# 設定登入帳號密碼（若無則可省略）
client.username_pw_set("timothy","123123123")

# 連線至 MQTT 伺服器（伺服器位址,連接埠）
client.connect("mqtt.ckcsc.net", 5900)

# 進入無窮處理迴圈
client.loop_forever()