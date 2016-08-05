#!/usr/bin/python


import threading
import sys
import time
import subprocess
import traceback

import serial
import wave



def play_audio(vol_level):
    filename = 'beep.wav'
    p = subprocess.Popen(['afplay','-v',str(vol_level),'robot.wav'])

def poll_serial():
    def play_with_delay(delay, vol_level, last_played):
        curr_time = time.time()
        delta = curr_time - last_played
        if delta > delay:
            play_audio(vol_level)
            print('just played')
            return True
        return False

    global sensor_avg
    sensor_avg = 0
    sensor_value = 0
    last_played = 0
    port = "/dev/cu.usbmodem1411"
    values = []
    ser = serial.Serial(port, baudrate=9600)

    while True:
        try:
            sensor_value = int(ser.readline())
        except:
            traceback.print_exc()
            sensor_value = 0
        print(str(sensor_value) + " " + str(sensor_avg))
        values.insert(0, sensor_value)
        if len(values) > 20:
            values = values[-1:]
        sensor_avg = sum(values)/len(values)
        if sensor_avg > 100:
            #if play_with_delay(50 - sensor_avg/10, sensor_avg/100, last_played):
            if sensor_avg > 500:
                if play_with_delay(.05, 100, last_played):
                    last_played = time.time()
            elif sensor_avg > 400:
                if play_with_delay(.1, 100, last_played):
                    last_played = time.time()
            elif sensor_avg > 300:
                if play_with_delay(.3, 1, last_played):
                    last_played = time.time()
            elif sensor_avg > 200:
                if play_with_delay(.4, .5, last_played):
                    last_played = time.time()
            elif sensor_avg > 100:
                if play_with_delay(1, .01, last_played):
                    last_played = time.time()
            elif sensor_avg > 50:
                print('here i am')
                if play_with_delay(1, .1, last_played):
                    last_played = time.time()
        """
        if sensor_avg > 500:
            play_with_delay(1)
        elif sensor_avg > 400:
            play_with_delay(2)
        elif sensor_avg > 300:
            play_with_delay(3)
        """          
            



#t = threading.Thread(target=poll_serial, args=())
#t.daemon = True
#t.start()

while True:
    poll_serial()



