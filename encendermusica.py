import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT) ##GPIO18 como salida musica
GPIO.output(23, True) #enciendo audio musica





