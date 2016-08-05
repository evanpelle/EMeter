#!/usr/bin/python

import redis
import sys
import subprocess

def play_audio(vol_level):
    filename = 'beep.wav'
    p = subprocess.Popen(['afplay','-v',str(vol_level),'res/el_ac.wav'])
values = []
has_played = False
r = redis.Redis()
print("sensor audio is starting up")
while True:
    if r.get('shutdown'):
        print('sensor audio shutting down')
        sys.exit(0)
    r = redis.Redis()
    sensor_value = float(r.get('sensor'))

    if sensor_value> 30 and not has_played:
        has_played = True
        play_audio(1)
    if sensor_value < 30:
        has_played = False



