import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
pomp=26
GPIO.setup(pomp,GPIO.OUT)

def pompa_apa_on():
    GPIO.output(pomp,GPIO.HIGH)

def pompa_apa_off():
    GPIO.output(pomp,GPIO.LOW)


    
