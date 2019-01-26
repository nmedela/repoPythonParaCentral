import RPi.GPIO as GPIO
import time
CERO=True ##EL 14 ES EL L6 1110 Y PONE DE ESTADO 0100 QUE ES ESTADO 4 (CASI APAGADO)
UNO=False
pulso=0.02
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(5,GPIO.OUT) ##GPIO5 como salida
GPIO.setup(6,GPIO.OUT) ##GPIO6 como salida
GPIO.setup(13,GPIO.OUT) ##GPIO13 como salida
GPIO.setup(19,GPIO.OUT) ##GPIO19 como salida
GPIO.output(5, UNO)
GPIO.output(6, UNO)
GPIO.output(13,UNO)
GPIO.output(19, CERO) ## PRIMERO SELECCIONO LA LUZ
time.sleep(pulso)
GPIO.output(5, CERO)
GPIO.output(6, CERO)
GPIO.output(13, CERO)
GPIO.output(19, CERO)
time.sleep(pulso)
GPIO.output(5, CERO)
GPIO.output(6, UNO)
GPIO.output(13, CERO)
GPIO.output(19, CERO)##DESPUES EL ESTADO
time.sleep(pulso)
GPIO.output(5, CERO)
GPIO.output(6, CERO)
GPIO.output(13, CERO)
GPIO.output(19, CERO)
