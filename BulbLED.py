from flux_led import *
import os

class BulbManagement():
    def __init__(self):
        self.my_input = ""
        # Search for bulbs.
        # os.system("python -m flux_led -s")

        # Turn on all bulbs on LAN. If this does not work, replace the -sS with the IP of the bulb.
        os.system("python -m flux_led -sS --on")

        while 1 == True:
            my_input = input("What color would you like? ")
            if my_input.lower() == "red":
                self.color_red()
            if my_input.lower() == "yellow":
                self.color_yellow()
            if my_input.lower() == "green":
                self.color_green()
            if my_input.lower() == "blue":
                self.color_blue()
    
    def color_red(self):
        # This should turn the bulb red. If not, first try replacing -sS with the IP of the bulb.
        return(os.system("python -m flux_led -sS -c '#FF0000'"))

    def color_yellow(self):
        # This should turn the bulb yellow.
        return(os.system("python -m flux_led -sS -c '#FFF700'"))
    
    def color_green(self):
        # This should turn the bulb green.
        return(os.system("python -m flux_led -sS -c '#00FF00'"))
    
    def color_blue(self):
        # This should turn the bulb green.
        return(os.system("python -m flux_led -sS -c '#0000FF'"))