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
   

def bluesaber():                                                                                     #Choose a Lightasber options are shown
    global led_colour
    led_colour[6] = (0,100,255);   led_colour[7] = (0,100,255)
    led_colour[65] =(0,100,255);   led_colour[66] = (0,100,255)
    led_colour[124] = (0,100,255); led_colour[125] = (0,100,255)
    led_colour[183] = (0,100,255); led_colour[184] = (0,100,255)
    led_colour[242] = (0,100,255); led_colour[243] = (0,100,255)
    
    led_colour[301] = (128,128,128); led_colour[302] = (128,128,128)

def greensaber():                                                                                     #Choose a Lightasber options are shown
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
    

def usersaber():
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


def scroll():                                                                               #Transitions from one state to another.
    led = 0
    while led<60:                                                                                  #scroll all rows at the same time
        for rows in range(6):
            led_colour[led+rows*60] = colour_choice[choice-1]
        update()
        time.sleep(.1)
        led = led+1

def transition():                                                                              #Transitions from one state to another.
    led = 0
    while led<60:                                                                                  #scroll all rows at the same time
        for rows in range(6):
            led_colour[led+rows*60] = (0,0,0)
        update()
        time.sleep(.03)
        led = led+1

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

def winner():
    prob=random.randrange(100)
    if prob<20:
        print("Congratulations, you won your duel. Thank you for playing")
    else:
        print("Sorry, you lost your duel. Thank you for playing")
       
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
    greensaber()
    purplesaber()
    yellowsaber()
    orangesaber()
    whitesaber()
    update() 
##    if available_colours[] == choice:
    break


    

choice = input('''Jedi welcome to your lightsaber fight. What is your lightsaber colour?
\t 1.Blue 
\t 2.Green
\t 3.Purple
\t 4.Yellow
\t 5.Orange
\t 6.White
Type the number of your selected choice and press Enter: ''')

print("You chose:", choice,"!")

available_colours = [1,2,3,4,5,6]
colour_choice = [(0,100,255),(0,255,50),(200,0,255),(255,255,0),(255,127,0),(255,255,255)]



while True:
    if choice.isdigit() == True:              
        choice = int(choice)                                                                        #If choice is a digit make it an integer instead of string
        if choice<1 or choice>6:                                                                    #value out of range
            choice = input("Please select an existing lightsaber choice: ")
            continue                                                                                #go back to .isdigit()        
        elif choice == available_colours[0]:                                                        #Here all ligh
            transition()
            bluesaber()
        elif choice == available_colours[1]:
            transition()
            greensaber()
        elif choice == available_colours[2]:
            transition()
            purplesaber()
        elif choice == available_colours[3]: 
            transition()
            yellowsaber()
        elif choice == available_colours[4]:
            transition()
            orangesaber()
        elif choice == available_colours[5]:
            transition()
            whitesaber()
        update() 
        time.sleep(2)
        scroll()
        transition()
        enemysaber()
        usersaber()
        vs()
        winner()
        break                                                             

                                                 

