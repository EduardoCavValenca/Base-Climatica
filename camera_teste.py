from picamera import PiCamera, Color
from time import sleep
from requests import get
import json
from pprint import pprint

url = "https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/966583"


weather = get(url).json()['items'][0]
pprint(weather)


camera = PiCamera()
camera.start_preview()

string = "Che - 11200421\n"
string += "Eduardo - 11234381\n\n"
string += f"Local: {weather['created_by']}\n"
string += f"Humidade: {weather['humidity']}\n"
string += f"Velocidade do Vento {weather['wind_speed']}\n"


camera.annotate_text = string
camera.capture('foto.jpg')
camera.start_recording('video.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()
