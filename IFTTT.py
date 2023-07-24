# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Importamos los módulos

import network, time, urequests
from machine import Pin, ADC
from utime import sleep, sleep_ms
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

#led_flash = Pin(4, Pin.OUT)
#led_flash.on()
#gc.collect()
#buf = tomar_foto()
#sleep(1)
#led_flash.off()

# Configura el pin de salida del sensor RCWL0516
pin_sensor = 14  # Reemplaza esto con el número de pin utilizado por tu ESP32
sensor = Pin(pin_sensor, Pin.IN)

# Variable para almacenar el estado de movimiento
movimiento = 0

# Variables de configuración de sensibilidad
sensibilidad_tiempo = 2  # Valor de tiempo de retardo en segundos (ajústalo según necesites)
sensibilidad_distancia = 3  # Valor de distancia de detección en metros (ajústalo según necesites)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Api solicitada:

    # url="https://api.thingspeak.com/update?api_key=03V8770SKW4TYMJY"

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Otros Ejemplos:

url= "https://maker.ifttt.com/trigger/Movimiento/with/key/btWwRnqZxN0ivEdwURcoA5YL1sESFL6jHgvhRjCWDJM?"
    # ir a la siguiente URL para la visualización  https://thingspeak.com/channels/2080912

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Código del sensor :
    #while True:
        #sensor_dht.measure()
        #tem = sensor_dht.temperature()
        #hum = sensor_dht.humidity()
        #print("Tem:{}°c, Hum:{}%".format(tem, hum))

def configurar_sensibilidad(tiempo, distancia):
    global sensibilidad_tiempo, sensibilidad_distancia
    sensibilidad_tiempo = tiempo
    sensibilidad_distancia = distancia

def detectar_movimiento():
    global movimiento
    # Lee el estado del pin del sensor (0 o 1)
    estado_pin = sensor.value()

    # Si el estado es 1 (movimiento detectado), asigna 1 a la variable "movimiento"
    if estado_pin == 1:
        movimiento = 1
        print ("Hay movimiento")
    else:
        movimiento = 0
        print("No hay movimiento")
detectar_movimiento()
    

while True:
    detectar_movimiento()

    # Puedes realizar cualquier acción o lógica adicional aquí con el valor de "movimiento"

    # Espera un breve período para evitar lecturas innecesarias y reducir la carga en la CPU
    time.sleep(sensibilidad_tiempo)
        
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Petición

        # respuesta = urequests.get(url+"&field1="+str(tem)+"&field2="+str(hum))# para thingspeak
    respuesta = urequests.get(url+"&value1="+str(movimiento))# para ifttt
    print(respuesta.text)
    print(respuesta.status_code)
    respuesta.close ()
    time.sleep(4)

 
else:
    print ("Imposible conectar")
    miRed.active (False)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>