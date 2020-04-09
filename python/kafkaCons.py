from kafka import KafkaConsumer
import pickle
import numpy as np
import serial
import ast
import sys
from matplotlib import pyplot as plt 
from matplotlib.animation import FuncAnimation
import time

np.set_printoptions(threshold=sys.maxsize)

if __name__ == '__main__':
  consumer = KafkaConsumer('capstone_project', auto_offset_reset='earliest',
                           bootstrap_servers=['localhost:9092'],
                           api_version=(0, 10),
                           consumer_timeout_ms=1000,
                           key_deserializer=lambda item: item.decode('utf-8') ,
                           value_deserializer=lambda item: item.decode('utf-8') ,

  )

for msg in consumer:
  frameStr= msg.value  #kafka message
  framenp  = eval ('np.array (' +  frameStr + ')') #numpy array from string
  #print(framenp.shape)
  #print(framenp.size)
  plt.xlabel('Color Intensity')   #X values
  plt.ylabel('Color Frequency')   #Y values
  plt.hist(framenp.ravel(),256,[0,256])  
  plt.title("Streaming Data Histogram")  #Title
  plt.show(block=False)
  plt.pause(0.003)
  plt.clf()
