import aubio
import numpy
from WifiBulb import WifiBulb
# from phue import Bridge
# import pyaudio This library hates me, I'll figure it out eventually
# import flux-led This library is not used rn
import wave

# import the class
from WifiBulb import WifiBulb

# create a new object and assign it's IP address
IP = "192.168.x.x"
myLightBulb = WifiBulb(IP)

# connect to the bulb
myLightBulb.connect()

# send it some colors
myLightBulb.setColor((255, 0, 0))

# disconnect when finished
myLightBulb.disconnect()