import RPi.GPIO as GPIO
import time
CERO=False ##EL 9 ES EL L1 1001 Y PONE DE ESTADO 0001 QUE ES ESTADO 1 (PRENDIDO$
UNO=True
pulso=1
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT) ##GPIO20 como salida
GPIO.output(27, UNO)

