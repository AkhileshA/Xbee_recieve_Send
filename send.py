import time
import pandas as pd
import numpy as np
import struct
from digi.xbee.devices import XBeeDevice
import serial
ser = serial.Serial('/dev/ttyUSB0')
sender = XBeeDevice("/dev/ttyUSB0", 9600)
sender.open()


df = pd.read_csv('example.csv')
lis=[]
for i in range(0, int(df.max()[0]) + 1):
    a = list(np.float32(df.iloc[i]))
    ba = bytearray()
    for j in range(1,len(a)):
        ba.extend(struct.pack('f',a[j]))
    lis.append(ba)
count =0
for i in range(0,9000):
    sender.send_data_broadcast(lis[i])
    count +=1
    print(count)
    '''time.sleep(0.1)'''
