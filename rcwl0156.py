from machine import Pin
import time

# Configura el pin de salida del sensor RCWL0516
pin_sensor = 14  # Reemplaza esto con el número de pin utilizado por tu ESP32
sensor = Pin(pin_sensor, Pin.IN)

# Variable para almacenar el estado de movimiento
movimiento = 0

# Variables de configuración de sensibilidad
sensibilidad_tiempo = 1  # Valor de tiempo de retardo en segundos (ajústalo según necesites)
sensibilidad_distancia = 3  # Valor de distancia de detección en metros (ajústalo según necesites)

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
        #print (movimiento)
    else:
        movimiento = 0
        #print(movimiento)
#detectar_movimiento()
    

#while True:
    #detectar_movimiento()

    # Puedes realizar cualquier acción o lógica adicional aquí con el valor de "movimiento"

    # Espera un breve período para evitar lecturas innecesarias y reducir la carga en la CPU
    time.sleep(sensibilidad_tiempo)
