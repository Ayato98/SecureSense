# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Importamos los módulos

import network, time, urequests
from machine import Pin, ADC
from utime import sleep, sleep_ms
from machine import ADC, Pin
import time

#from dht import DHT22

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Conectando a la red con WIFI

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

if conectaWifi ("BlackHard", "Black98//"):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())

    
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Creamos el objeto


led = Pin(2, Pin.OUT) # Define el pin del LED
sensor = ADC(Pin(13)) # Define el pin analógico del sensor

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Api solicitada:

    # url="https://api.thingspeak.com/update?api_key=03V8770SKW4TYMJY"

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Otros Ejemplos:

url= "https://maker.ifttt.com/trigger/deteccion_mq2/with/key/btWwRnqZxN0ivEdwURcoA5YL1sESFL6jHgvhRjCWDJM?"
    # ir a la siguiente URL para la visualización  https://thingspeak.com/channels/2080912

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Código del sensor :
    #while True:
        #sensor_dht.measure()
        #tem = sensor_dht.temperature()
        #hum = sensor_dht.humidity()
        #print("Tem:{}°c, Hum:{}%".format(tem, hum))

while True:
    lectura = sensor.read() # Lee el valor del sensor
    voltaje = (lectura*5)/1023 # Convierte la lectura en voltaje
    gas_licuado = (voltaje/1.1)*1000 # Convierte el voltaje en concentración de gas licuado (ppm)
    humo = (voltaje/1.05)*1000 # Convierte el voltaje en concentración de humo (ppm)
    dioxido_carbono = (voltaje/1.2)*1000 # Convierte el voltaje en concentración de dióxido de carbono (ppm)
    
           # print("Gas licuado: ", gas_licuado, "ppm")
        #print("Humo: ", humo, "ppm")
        #print("Dióxido de carbono: ", dioxido_carbono, "ppm")
            #or humo > 2000 or dioxido_carbono > 2000
    if gas_licuado > 14000 : # Si la concentración de gas supera los 2000 ppm, enciende el LED
        print("Gas licuado: ", gas_licuado, "ppm")
        print("Intoxicacion por Gas\n")
            
    elif humo > 15000:
                #led.value(0)
        print("Humo: ", humo, "ppm")
        print("Intoxicacion por humo\n")
            
    elif dioxido_carbono > 13000:
        print("Dióxido de carbono: ", dioxido_carbono, "ppm")
        print("Intoxicacion por dioxido de carbono\n")
            
    else:
        print("Aire limpio")
    
    time.sleep(1) # Espera 1 segundo antes de volver a leer el sensor
        
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Petición

        # respuesta = urequests.get(url+"&field1="+str(tem)+"&field2="+str(hum))# para thingspeak
    respuesta = urequests.get(url+"&value1="+str(gas))# para ifttt
    print(respuesta.text)
    print(respuesta.status_code)
    respuesta.close ()
    time.sleep(4)

 
#        else:
 #           print ("Imposible conectar")
 #           miRed.active (False)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>