#!/bin/sh

./shutdown.sh

(redis-server &)

redis-cli del shutdown

if [ "$1" = "r" ]; then
    Arduino --upload /Users/evan/Desktop/r2r/ard/ard.ino
fi

(./poll_serial.py &)

(./sensor_audio.py &)

(./plot_sensor.py &)

