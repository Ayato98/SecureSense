

from machine import Pin, ADC
import urequests
import network
import time
from utime  import sleep, sleep_ms, ticks_ms
import rcwl0156 as movimiento
#from utelegram import Bot
import cam
from webcam import server
#import mejorlectura as aire
import ufirebase as firebase



#TOKEN = '6505565647:AAEidPs_j9zw9w6SVU2_8j-UcEacPut_xTQ'
#bot = Bot(TOKEN)
#led = Pin(2, Pin.OUT)
red = "BlackHard"
password = "Black98//"
#sensor = ADC(Pin(13))

firebase.setURL ("https://sense-896b2-default-rtdb.firebaseio.com/")
#def gas():
    #while True:
    #lectura = sensor.read() # Lee el valor del sensor
    #voltaje = (lectura*3.3)/1023 # Convierte la lectura en voltaje
    #gas_licuado = (voltaje/1.1)*1000 # Convierte el voltaje en concentración de gas licuado (ppm)
    #humo = (voltaje/1.05)*1000 # Convierte el voltaje en concentración de humo (ppm)
    #dioxido_carbono = (voltaje/1.2)*1000 # Convierte el voltaje en concentración de dióxido de carbono (ppm)
    
    #print("Gas licuado: ", gas_licuado, "ppm")
    #print("Humo: ", humo, "ppm")
    #print("Dióxido de carbono: ", dioxido_carbono, "ppm")
            #or humo > 2000 or dioxido_carbono > 2000
        #if gas_licuado > 2000 : # Si la concentración de gas supera los 2000 ppm, enciende el LED
            #led.value(1)
            #print("peligro")
            #if dioxido_carbono >5000:
             #   print("peligro dioxido de carbono")
        #else:
            #led.value(0)
    
    #time.sleep(1) # Espera 1 segundo antes de volver a leer el sensor
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
    
    
if conectaWifi("BlackHard", "Black98//"):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
    #url = "https://api.thingspeak.com/update?api_key=QMPZM9YDQNTA2KD6"
    url = "https://maker.ifttt.com/trigger/Movimiento/with/key/btWwRnqZxN0ivEdwURcoA5YL1sESFL6jHgvhRjCWDJM?"
    #url = "https://maker.ifttt.com/trigger/Movimiento/with/key/bEouoRqOod31W0aZrdNpP8?"
    #@bot.add_message_handler('Hola')
    #def help(update):
    #    update.reply("buenos diaxxx")
    #if movimiento.mov == 1:
    #    @bot.add_message_handler('1')
    #    def help(update):
    #        update.reply("buenos diaxxx")
    #        bot.start_loop()
    while True:
        movimiento.detectar_movimiento()
        if movimiento.movimiento==1:
            print("Foto tomada")
            cam.ejecucion()
            x = movimiento.movimiento
            sleep(5)
        
        with open("/Foto.jpeg", "rb") as archivo_imagen:
            imagen = archivo_imagen.read()
            #nombre_imagen = "foto_{}.jpg".format(ticks_ms())
            
        with open(server):
            server = server.read()


            message = {"Movimiento": "Hay movimiento"}
            firebase.put("hogar/movimiento,{}".format(ticks_ms()), message, bg=0)
        
            respuesta = urequests.get(url+"&value1="+str(movimiento.movimiento)+"&value2="+str(server))
            print(respuesta.text)
            print(respuesta.status_code)
            respuesta.close ()
        
        
    #humo = mejorlectura.gas.humo
    #dc = mejorlectura.gas.dioxido_carbono
    #respuesta = urequests.get(url+"&field1="+str(gasl)+"&field2="+str(humo)+"&field3="+str(dc))# para thingspeak
    #respuesta = urequests.get(url+"&value1="+str(gasl)+"&value2="+str(humo)+"&value3="+str(dc))# para ifttt
    #print(humo)
        
    #print(dc)
    #respuesta.close ()
    
    #time.sleep(4)
    
    #medir.gas()