# Streaming Server
# Echo server program
import socket
import struct
import cv2
import pickle
import sys
from kafka import KafkaConsumer, KafkaProducer
import json
import numpy as np

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8083




np.set_printoptions(threshold=sys.maxsize)

def publish_message(producer_instance, topic_name, key, value):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        producer_instance.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))


def connect_kafka_producer():
    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))        
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer

kafka_producer = connect_kafka_producer()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(10)
    conn, addr = s.accept()    
    data = b''
    payloadSize = struct.calcsize("L")
    with conn:
        print('Connected by', addr)
        while True:
            while len(data) < payloadSize:
                data += conn.recv(4096)
                if not data: break
            packed_msg_size = data[:payloadSize]
            data = data[payloadSize:]
            msg_size = struct.unpack("L", packed_msg_size)[0]
            while len(data) < msg_size:
                data += conn.recv(4096)
            frame_data = data[:msg_size]
            data = data[msg_size:]
            frame=pickle.loads(frame_data)
            print(frame)
            print(type(frame))
            framestr=np.array2string(frame, precision=2, separator=',', suppress_small=True)
            publish_message(kafka_producer, 'capstone_project', 'raw', framestr)
           # cv2.imshow('frame', frame)
           # cv2.waitKey(10)
