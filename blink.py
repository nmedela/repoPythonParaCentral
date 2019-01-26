import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT) ##GPIO17 como salida
GPIO.setup(27,GPIO.OUT) ##GPIO27 como salida
GPIO.output(17, True)
		#GPIO.output(27, False)
		#time.sleep(1)
		#GPIO.output(17, False)
		#GPIO.output(27, True)         
		#time.sleep(1)               
		
		

#Y liberamos los GPIO
