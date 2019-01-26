import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT) #GPIO17 como salida
GPIO.output(17, False)   #GPIO17 apaga
