import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18,GPIO.OUT) ##GPIO18 como salida indica si hay que atenuar
GPIO.setup(27,GPIO.OUT) ##GPIO27 como salida
GPIO.setup(22,GPIO.OUT) ##GPIO22 como salida


GPIO.output(18, True)
GPIO.output(27, False)
GPIO.output(22, False)

	
#GPIO.output(18, not GPIO.input(18))
