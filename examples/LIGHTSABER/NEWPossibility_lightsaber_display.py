##Idea to use list instead of functions
import opc
import time
import random
import colorsys

#BACKGROUND
led_colour = [(0,0,0)]*360                                                                          #Creates background to start

client = opc.Client('localhost:7890')


client.put_pixels(led_colour)
client.put_pixels(led_colour)

#FUNCTIONS
def update():                                                                                        #Automatically updates what the code is doing. No need to repeat it all the time
    client.put_pixels(led_colour)
    client.put_pixels(led_colour)

bluesaber = [6,7,65,66,124,125,183,184,242,243,301,302]

led = 0

while led<360:
    for x in bluesaber:
        led_colour = (0,0,255)

