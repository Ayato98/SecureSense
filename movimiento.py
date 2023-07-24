from machine import Pin
import time
from utelegram import Bot

# Configuración de los pines
out_pin = Pin(14,Pin.IN)
TOKEN = '6398415723:AAG2F7OYQGveyTmKpsEELEFAwpzb_J8hqiY'
bot = Bot(TOKEN)
#cds_pin = machine.ADC(machine.Pin(36))
# Función para leer el estado del sensor de movimiento
def read_motion_sensor():
    return out_pin.value()

# Función para leer el valor del detector de luz
#def read_light_sensor():
#    return cds_pin.read()
movi = 1

# Bucle principal
while True:
    # Lee el estado del sensor de movimiento
    motion = read_motion_sensor()

    # Lee el valor del detector de luz (CDS)
    #light_value = read_light_sensor()

    # Imprime los resultados
    if motion:
        #print("Movimiento detectado", motion)
        movi = 1
        

                
    else:
        #print("Sin movimiento", motion)
        movi = motion        
    #print("Valor del detector de luz: {}".format(light_value))

    # Espera un segundo antes de tomar la siguiente lectura
        print(movi)   

        time.sleep(1)



