import machine
import network
import urequests as requests
from machine import SoftSPI
from ssd1306 import SSD1306_SPI
from machine import UART
import esp32
from machine import Timer
from machine import reset
import os
import ujson

# Configuración de la conexión WiFi
SSID = "nombre_de_la_red_wifi"
PASSWORD = "contraseña_de_la_red_wifi"

# Configuración del bot de Telegram
TELEGRAM_BOT_TOKEN = "tu_token_del_bot"
CHAT_ID = "tu_chat_id"

# Configuración del ESP32-CAM
CAMERA_CAPTURE_PIN = 4  # Pin donde se encuentra el botón de captura de la cámara
PHOTO_FILE_PATH = "/photo.jpg"  # Ruta donde se guardará la foto

# Configuración de la URL de la API de Telegram para enviar mensajes con fotos
TELEGRAM_API_URL = "https://api.telegram.org/bot{}/sendPhoto".format(TELEGRAM_BOT_TOKEN)

# Inicializar la cámara
import gc
gc.collect()
try:
    import sensor
    sensor.reset()
    sensor.set_pixformat(sensor.JPEG)
    sensor.set_framesize(sensor.VGA)
    sensor.skip_frames(time=2000)
except Exception as e:
    print("Error initializing the camera:", e)
    raise

# Inicializar el módulo ESP32-CAM
uart = UART(2, rx=17, tx=16, timeout=100)
nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect(SSID, PASSWORD)

# Esperar a que se establezca la conexión WiFi
while not nic.isconnected():
    time.sleep_ms(100)

# Función para capturar y enviar la foto al bot de Telegram
def capture_and_send_photo():
    try:
        # Capturar la foto
        img = sensor.snapshot()

        # Guardar la foto en la tarjeta SD (opcional)
        img.save(PHOTO_FILE_PATH)

        # Enviar la foto al bot de Telegram
        files = {"photo": open(PHOTO_FILE_PATH, "rb")}
        data = {"chat_id": CHAT_ID}
        response = requests.post(TELEGRAM_API_URL, files=files, data=data)
        if response.status_code == 200:
            print("Foto enviada correctamente.")
        else:
            print("Error al enviar la foto:", response.text)
    except Exception as e:
        print("Error en la captura y envío de la foto:", e)

# Configurar el botón de captura de la cámara
capture_button = Pin(CAMERA_CAPTURE_PIN, Pin.IN)

# Función para manejar la interrupción del botón de captura
def capture_button_interrupt_handler(pin):
    if not pin.value():  # Verificar que el botón esté presionado
        print("Botón de captura presionado.")
        capture_and_send_photo()

# Configurar la interrupción del botón de captura
capture_button.irq(trigger=Pin.IRQ_FALLING, handler=capture_button_interrupt_handler)

# Bucle principal
while True:
    time.sleep(1)