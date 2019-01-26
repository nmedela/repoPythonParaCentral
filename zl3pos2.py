import RPi.GPIO as GPIO
import time
CERO=True ##EL 11 ES EL L3 1001 Y PONE DE ESTADO 0011 QUE ES ESTADO 3 (prendido a la mitad)
UNO=False
pulso=0.02
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(5,GPIO.OUT) ##GPIO5 como salida
GPIO.setup(6,GPIO.OUT) ##GPIO6 como salida
GPIO.setup(13,GPIO.OUT) ##GPIO13 como salida
GPIO.setup(19,GPIO.OUT) ##GPIO19 como salida
GPIO.output(5, UNO)
GPIO.output(6, CERO)
GPIO.output(13,UNO)
GPIO.output(19, UNO) ## PRIMERO SELECCIONO LA LUZ
time.sleep(pulso)
GPIO.output(5, CERO)
GPIO.output(6, CERO)
GPIO.output(13, CERO)
GPIO.output(19, CERO)
time.sleep(pulso)
GPIO.output(5, CERO)
GPIO.output(6, CERO)
GPIO.output(13, UNO)
GPIO.output(19, UNO)##DESPUES EL ESTADO
time.sleep(pulso)
GPIO.output(5, CERO)
GPIO.output(6, CERO)
GPIO.output(13, CERO)
GPIO.output(19, CERO)
