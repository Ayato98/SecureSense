from machine import Pin
from time import *
# https://github.com/lemariva/micropython-camera-driver
import camera
import gc
import machine
import network
import urequests as requests
from machine import SoftSPI
from machine import UART
import esp32
from machine import Timer
from machine import reset
import os
import ujson

# LED integrado
"""
led_flash = Pin(4, Pin.OUT)
led_flash.on()
sleep(1)
led_flash.off()
""" 

def tomar_foto(nombre= 'Foto.jpeg', voltear= 0, espejo= 1):    
    camera.init(0, format=camera.JPEG, fb_location=camera.PSRAM)    
    camera.framesize(camera.FRAME_240X240)
    #camera.framesize(camera.FRAME_VGA)    
    camera.flip(voltear)
    camera.mirror(espejo)    
    buf = camera.capture()    
    f = open(nombre, "wb")
    f.write(buf)
    f.close()
    camera.deinit()
    return buf


led_flash = Pin(4, Pin.OUT)
led_flash.on()
gc.collect()
buf = tomar_foto()
sleep(1)
led_flash.off()
