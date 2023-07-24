

from machine import Pin
import network
from utime  import sleep, sleep_ms

#import rcwl0156 as movimiento
from utelegram import Bot
#import mejorlectura

TOKEN = '6398415723:AAG2F7OYQGveyTmKpsEELEFAwpzb_J8hqiY'
bot = Bot(TOKEN)
led = Pin(2, Pin.OUT)

red = "esp32"
password = "1234abcd"


def conectaWifi (red, password):
      global miRed
      miRed = network.WLAN(network.STA_IF)     
      if not miRed.isconnected():              #Si no está conectado…
          miRed.active(True)                   #activa la interface
          miRed.connect(red, password)         #Intenta conectar con la red
          print('Conectando a la red', red +"…")
          timeout = time.time ()
          while not miRed.isconnected():           #Mientras no se conecte..
              if (time.ticks_diff (time.time (), timeout) > 10):
                  return False
      return True
    
    
if conectaWifi("esp32", "1234abcd"):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
    
    @bot.add_message_handler('Hola')
    def help(update):
        update.reply("buenos diaxxx")
    #if movimiento.mov == 1:
    #    @bot.add_message_handler('1')
    #    def help(update):
    #        update.reply("buenos diaxxx")
    #        bot.start_loop()
            


#while True:
    
   # print("\n")
   # sleep(1)
    #medir.gas()