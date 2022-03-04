#LIBRARIES

import opc
import time
import random
import math
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

#animation of enemy igniting lightsaber
def enemysaber():                                                                                    #Choose a Lightasber options are shown
    led_colour[354] = (128,128,128);  led_colour[356] = (128,128,128)
    #Igniting blade
    update()
    time.sleep(0.5)
    led_colour[294] = (255,0,0); led_colour[296] = (255,0,0);
    update()
    time.sleep(0.03)
    led_colour[234] = (255,0,0); led_colour[236] = (255,0,0);
    update()
    time.sleep(0.03)
    led_colour[174] = (255,0,0); led_colour[176] = (255,0,0);
    update()
    time.sleep(0.03)
    led_colour[114] = (255,0,0); led_colour[116] = (255,0,0);
    update()
    time.sleep(0.03)
    led_colour[54] = (255,0,0); led_colour[56] = (255,0,0);
    update()
    time.sleep(0.03)
    
#animation ignite your lightsaber
def usersaber(choice):
    led_colour[304] = (128,128,128);  led_colour[306] = (128,128,128)
    #Igniting blade
    update()
    time.sleep(0.5)
    led_colour[244] = colour_choice[choice-1]; led_colour[246] = colour_choice[choice-1];
    update()
    time.sleep(0.03)
    led_colour[184] = colour_choice[choice-1]; led_colour[186] = colour_choice[choice-1];
    update()
    time.sleep(0.03)
    led_colour[124] = colour_choice[choice-1]; led_colour[126] = colour_choice[choice-1];
    update()
    time.sleep(0.03)
    led_colour[64] = colour_choice[choice-1]; led_colour[66] = colour_choice[choice-1];
    update()
    time.sleep(0.03)
    led_colour[4] = colour_choice[choice-1]; led_colour[6] = colour_choice[choice-1];
    update()
    time.sleep(0.03)
 
#animation of VS blinking
def vs(vs_leds):
    led_colour[3]= (255,255,0)

#animation of your lightsaber moving towards enemy
def dueluser():
    if led_colour == animation:
        rednight_protocol 
    
    
def vs():
    vs_list = [21,22,29,30,31,32,33,34,35,36,37,82,83,88,89,91,143,144,147,148,151,152,153,154,155,156,157,204,205,206,207,217,265,266,271,272,273,274,275,276,277]
    for p in vs_list:
        led_colour[p] = (255,255,0)
        update
        time.sleep(0.1)
        led_colour[p] = (0,0,0)
        time.sleep(0.1)
        led_colour[p] = (255,255,0)
        update()
    
    
    


#code
available_colours = [1,2,3,4,5,6]

colour_choice = [(0,100,255),(0,255,50),(200,0,255),(255,255,0),(255,127,0),(255,255,255)]

while True:
    enemysaber()
    usersaber(3)
    vs()
    update()
    time.sleep(5)
    break


    
    
    
    
