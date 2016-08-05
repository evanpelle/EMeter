#!/usr/bin/python

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api
import time
import sys
import numpy as np

import plotly.plotly as py
from plotly.graph_objs import *
import plotly.tools as tls
from datetime import datetime

import redis

r = redis.Redis()

tls.set_credentials_file(stream_ids=[
                'a1kp6ml6e5',
                'soa3n6g6uu',
                'vmv28dohb7',
                'kq89yvlk7r'
            ])

stream_ids = tls.get_credentials_file()['stream_ids']
stream_id = stream_ids[0]


x = [
    datetime(year=2013, month=10, day=04),
    datetime(year=2013, month=11, day=05),
    datetime(year=2013, month=12, day=06)
]




stream = Stream(
    token=stream_id,
    maxpoints=80
)

data = Data([
    Scatter(
        x=[],
        y=[],
        stream=stream
    )
])


plot_url = py.plot(data, filename='python-datetime')

s = py.Stream(stream_id)

# (@) Open the stream
s.open()


# Delay start of stream by 5 sec (time to switch tabs)
time.sleep(5)

while True:

    if r.get('shutdown'):
        print('plot_sensor.py is shutting down')
        sys.exit(0)

    # Current time on x-axis, random numbers on y-axis
    x = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    #y = (np.cos(k*i/50.)*np.cos(i/50.)+np.random.randn(1))[0]
    y = float(r.get('sensor'))
    # (-) Both x and y are numbers (i.e. not lists nor arrays)

    # (@) write to Plotly stream!
    s.write(dict(x=x, y=y))

    # (!) Write numbers to stream to append current data on plot,
    #     write lists to overwrite existing data on plot (more in 7.2).

    time.sleep(0.08)  # (!) plot a point every 80 ms, for smoother plotting

# (@) Close the stream when done plotting
s.close()
