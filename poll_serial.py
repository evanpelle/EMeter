#!/usr/bin/python


import threading
import sys
import time
import subprocess
import traceback

import redis
import serial



if __name__ == '__main__':
    sensor_avg = 0
    sensor_value = 0
    port = "/dev/cu.usbmodem1411"
    values = []
    ser = serial.Serial(port, baudrate=9600)
    r = redis.Redis()
    try:
        ser.readline()
        print("poll_serial connection created and functional")
    except:
        print("error creating serial connection")
        traceback.print_exc()
    while True:
        if r.get('shutdown'):
            print('poll_serial is shutting down')
            sys.exit(0)
        try:
            sensor_value = int(ser.readline())
        except:
            traceback.print_exc()
            sensor_value = 0
        values.insert(0, sensor_value)
        if len(values) > 20:
            values = values[:-1]
        sensor_avg = sum(values)/len(values)
        r.set('sensor', sensor_avg)


