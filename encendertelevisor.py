import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT) ##GPIO18 como salida musica
GPIO.setup(24,GPIO.OUT) ##GPIO27 como salida televisor

GPIO.output(23, False) #apago audio musica
GPIO.output(24, True) #enciendo audio televisor




