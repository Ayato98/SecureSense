from machine import ADC, Pin
#from BaseMQ import BaseMQ
from micropython import const
import time

led = Pin(2, Pin.OUT) # Define el pin del LED
sensor = ADC(Pin(13)) # Define el pin analógico del sensor

while True:
    lectura = sensor.read() # Lee el valor del sensor
    voltaje1 = (lectura*2.95)/1023 # Convierte la lectura en voltaje
    voltaje2 = (lectura*3.54)/1023
    voltaje3 = (lectura*3.10)/1023
    gas_licuado = (voltaje1 / 1.1) * 1000 # Convierte el voltaje en concentración de gas licuado (ppm)
    humo = (voltaje2 / 1.05) * 1000 # Convierte el voltaje en concentración de humo (ppm)
    dioxido_carbono = (voltaje3 / 1.2) * 1000 # Convierte el voltaje en concentración de dióxido de carbono (ppm)
        
          
    if gas_licuado > 2800: # Si la concentración de gas supera los 2000 ppm, enciende el LED
            #led.value(1)
        print("Gas licuado: ", gas_licuado, "ppm")
        print("Intoxicacion por Gas\n")
        
    elif humo > 2500:
                #led.value(0)
        print("Humo: ", humo, "ppm")
        print("Intoxicacion por humo\n")
            
    elif dioxido_carbono > 2400:
        print("Dióxido de carbono: ", dioxido_carbono, "ppm")
        print("Intoxicacion por dioxido de carbono\n")
            
    else:
        print("Aire limpio")
            
    
    time.sleep(1) # Espera 1 segundo antes de volver a leer el sensor
gas()
