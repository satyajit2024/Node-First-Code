from mqtt_update import MqttConnect
import time
from datetime import datetime
from random import uniform
from paho.mqtt.client import Client
import threading
from recive import recive
import redis
redis_server = redis.Redis(host="localhost",port=6379,db=0)


mq = MqttConnect()
mq.topic = ["578689832956829"]

def post_data_to_publish():
    mq.connect_to_broker()
    while True:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for i in mq.topic:
            current = float(redis_server.get("current").decode('utf-8'))
            mq.data_publish({"dataPoint": now, "paramType": 'current', "paramValue": current , "deviceId": i})

        time.sleep(5)



def data_subscribe():
    mqtt_client = Client()
    mqtt_client.on_connect = mq.on_connect
    mqtt_client.on_message = mq.on_sub_message
    mqtt_client.username_pw_set(mq._username, mq._password)
    mqtt_client.connect(mq._mqttBroker, port=mq._port)
    mqtt_client.loop_start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        mqtt_client.loop_start()



if __name__ == '__main__':
    threading.Thread(target=post_data_to_publish).start()
    threading.Thread(target=data_subscribe).start()
    threading.Thread(target=recive).start()