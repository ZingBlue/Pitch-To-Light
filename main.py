#import aubio
#import numpy
#import webcolors
from WifiBulb import WifiBulb
# from phue import Bridge
# import pyaudio This library hates me, I'll figure it out eventually
# import flux-led This library is not used rn
import time

# import the class

# create a new object and assign it's IP address
IP_king = "192.168.42.20"
IP_smort = "192.168.42.19"
right = WifiBulb(IP_king)
left = WifiBulb(IP_smort)

# connect to the bulb
left.connect()
right.connect()
# time.sleep(5) bad man
# send it some colors
left.setColor([0,0,50])
right.setColor([0,225,0])
time.sleep(5)
#left.warmwhite()
#time.sleep(5)
#time.sleep(2)
#Preset colors just yeah

#def red(bulb):
#        bulb.setColor((255,0,0))

#def green(bulb):
#        bulb.setColor((0,255,0))       
#def blue(bulb):
#        bulb.setColor((0,0,225))        
#def white(bulb):
#        bulb.warmwhite(255)        
#color change
#while(False):
#    red(left)
#    green(right)
#    
#    time.sleep(5)
#    
#    green(left)
#    blue(right)
#    
#    time.sleep(5)
#    
#    blue(left)
#    white(right)
#    
#    time.sleep(5)
#    
#    white(left)
#    red(right)
#    
#    time.sleep(5)
# disconnect when finished
right.disconnect()
left.disconnect()