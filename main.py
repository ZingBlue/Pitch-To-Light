import aubio
import numpy
from phue import Bridge
# import pyaudio This library hates me, I'll figure it out eventually
import wave

b = Bridge('0.0.0.0') # The IP of the light bulb

b.connect() # This only needs to run once, it connects the bulb


"""
arg is lamp number (if you have several lights I think)
arg2 is the setting changed (in this case brightness)
arg3 is the value 254 is maximum brightness, 0 is smalliest.
"""
b.set_light(1, 'bri', 254)