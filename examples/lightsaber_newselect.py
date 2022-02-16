import opc
import time
import random
import colorsys

leds = [(255,255,255)]*360

client = opc.Client('localhost:7890')



client.put_pixels(leds)
client.put_pixels(leds)
