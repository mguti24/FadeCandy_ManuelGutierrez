#LIBRARIES

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


def bluesaber():                                                                                     #Choose a Lightasber options are shown
    global led_colour
    led_colour[6] = (0,100,255);   led_colour[7] = (0,100,255)
    led_colour[65] =(0,100,255);   led_colour[66] = (0,100,255)
    led_colour[124] = (0,100,255); led_colour[125] = (0,100,255)
    led_colour[183] = (0,100,255); led_colour[184] = (0,100,255)
    led_colour[242] = (0,100,255); led_colour[243] = (0,100,255)
    led_colour[301] = (128,128,128); led_colour[302] = (128,128,128)

def greensaber(delay):                                                                                     #Choose a Lightasber options are shown
    global led_colour
    led_colour[16] = (0,255,50);   led_colour[17] = (0,255,50)
    led_colour[75] =(0,255,50);   led_colour[76] = (0,255,50)
    led_colour[134] = (0,255,50); led_colour[135] = (0,255,50)
    led_colour[193] = (0,255,50); led_colour[194] = (0,255,50)
    led_colour[252] = (0,255,50); led_colour[253] = (0,255,50)
    led_colour[311] = (128,128,128); led_colour[312] = (128,128,128)

def purplesaber():                                                                                    #Choose a Lightasber options are shown
    global led_colour
    led_colour[26] = (200,0,255);   led_colour[27] = (200,0,255)
    led_colour[85] =(200,0,255);   led_colour[86] = (200,0,255)
    led_colour[144] = (200,0,255); led_colour[145] = (200,0,255)
    led_colour[203] = (200,0,255); led_colour[204] = (200,0,255)
    led_colour[262] = (200,0,255); led_colour[263] = (200,0,255)
    led_colour[321] = (128,128,128); led_colour[322] = (128,128,128)

def yellowsaber():                                                                                    #Choose a Lightasber options are shown
    global led_colour
    led_colour[36] = (255,255,0);   led_colour[37] = (255,255,0)
    led_colour[95] =(255,255,0);   led_colour[96] = (255,255,0)
    led_colour[154] = (255,255,0); led_colour[155] = (255,255,0)
    led_colour[213] = (255,255,0); led_colour[214] = (255,255,0)
    led_colour[272] = (255,255,0); led_colour[273] = (255,255,0)
    led_colour[331] = (128,128,128); led_colour[332] = (128,128,128)

def orangesaber():                                                                                    #Choose a Lightasber options are shown
    global led_colour
    led_colour[46] = (255,127,0);   led_colour[47] = (255,127,0)
    led_colour[105] =(255,127,0);   led_colour[106] = (255,127,0)
    led_colour[164] = (255,127,0); led_colour[165] = (255,127,0)
    led_colour[223] = (255,127,0); led_colour[224] = (255,127,0)
    led_colour[282] = (255,127,0); led_colour[283] = (255,127,0)
    led_colour[341] = (128,128,128); led_colour[342] = (128,128,128)

def whitesaber():                                                                                    #Choose a Lightasber options are shown
    global led_colour
    led_colour[56] = (255,255,255);   led_colour[57] = (255,255,255)
    led_colour[115] =(255,255,255);   led_colour[116] = (255,255,255)
    led_colour[174] = (255,255,255); led_colour[175] = (255,255,255)
    led_colour[233] = (255,255,255); led_colour[234] = (255,255,255)
    led_colour[292] = (255,255,255); led_colour[293] = (255,255,255)
    led_colour[351] = (128,128,128); led_colour[352] = (128,128,128)



    

def transition(delay):                                                                               #Transitions from one state to another.
    global led_colour                                                                                #Create/use global variable "led_colour"
    for p in range (0, 60):
        led_colour[p] = (255,255,0)
        led_colour[p+60] = (128,128,128)
        led_colour[p+120] = (255,255,0)
        led_colour[p+180] = (128,128,128)
        led_colour[p+240] = (255,255,0)
        led_colour[p+300] = (128,128,128)
        
     

    
    
##blue (0,100,255)
##green (0,255,50)
##purple (255,0,255)
##yellow (255,255,0)
##orange (255,127,0)
##white (255,255,255)
##grey (128,128,128)


#CODE

led = 0

while led<360:
    bluesaber()
    greensaber(5)
    purplesaber()
    yellowsaber()
    orangesaber()
    whitesaber()
    time.sleep(.1)
    update() 
    break

    

choice = input("Jedi welcome to your lightsaber fight. What is your lightsaber colour?")
print("You chose:", choice,"!")

available_colours = [blue,green,purple,yellow,orange,white] 


    

    

##while led<60:
##        leds = (0,0,255)
##        client.put_pixels(leds)
##        time.sleep(.1)    
##    break
