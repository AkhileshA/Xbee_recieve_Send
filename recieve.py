import time
import pandas as pd
import numpy as np
import struct
from digi.xbee.devices import XBeeDevice
import serial
reciever = XBeeDevice("/dev/ttyUSB1", 9600)
reciever.open()
while 1:
    a = None
    while a==None:
        a=reciever.read_data()
    dat = a.data
    dat=dat.hex()
    temp = list()
    curr =''
    p = 1
    for i in range(0,72):
        if ((i)%8 == 0 or i == 71):
            if (i == 71):
                curr += dat[i]
            if (curr != ''):
                temp.append(curr)
            curr=''
        curr += dat[i]

    arr = list()
    for i in temp:
        x = bytearray()
        x = x.fromhex(i)
        arr.append(struct.unpack('f',x)[0])
    print(arr)
