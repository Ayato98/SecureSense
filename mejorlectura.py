from machine import ADC, Pin
import time

led = Pin(2, Pin.OUT) # Define el pin del LED
sensor = ADC(Pin(13)) # Define el pin analógico del sensor

def gas():
    while True:
        lectura = sensor.read() # Lee el valor del sensor
        voltaje = (lectura*3.3)/1023 # Convierte la lectura en voltaje
        gas_licuado = (voltaje/1.1)*1000 # Convierte el voltaje en concentración de gas licuado (ppm)
        humo = (voltaje/1.05)*1000 # Convierte el voltaje en concentración de humo (ppm)
        dioxido_carbono = (voltaje/1.2)*1000 # Convierte el voltaje en concentración de dióxido de carbono (ppm)
    
           # print("Gas licuado: ", gas_licuado, "ppm")
        #print("Humo: ", humo, "ppm")
        #print("Dióxido de carbono: ", dioxido_carbono, "ppm")
            #or humo > 2000 or dioxido_carbono > 2000
        if gas_licuado > 2000 : # Si la concentración de gas supera los 2000 ppm, enciende el LED
            led.value(1)
            #print("peligro")
            #if dioxido_carbono >5000:
             #   print("peligro dioxido de carbono")
        else:
            led.value(0)
    
        time.sleep(1) # Espera 1 segundo antes de volver a leer el sensor
    
