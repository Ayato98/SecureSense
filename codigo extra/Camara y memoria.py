import machine
from machine import Pin
import time
import camera
import uos
import sdcard

flash = Pin(4, Pin.OUT)
flash.value(1)
time.sleep(1)
flash.value(0)

#uos.mount(sdcard.SDCard(), "/sd")

#sd = machine.SDCard(slot=2)
#vfs=os.VfsFat(sd)
#os.mount(vfs, "/sd")  # mount

#os.listdir('/sd')    # list directory contents

count = 0

def tomar_foto(nombre= 'Foto.jpeg', voltear= 0, espejo= 1):
    if count == 5 :
        flash.value(1)
        print("capture the images")
    camera.init(0, format=camera.JPEG, fb_location=camera.PSRAM)
    camera.flip(voltear)
    camera.mirror(espejo)    
    buf = camera.capture()    
    f = open(nombre, "w")
    f.write(buf)
    f.close()
    camera.deinit()
        
    count += 1
    time.sleep(1)
    

    #buf = camera.capture()
    #file = open('/sd/'+str(count)+'.jpeg', 'w')
    #file.write(buf)
    #file.close()
    #print(str(count)+'.jpeg is captured')
    
    print("done all the work")