import RPi.GPIO as GPIO
import time
CERO=False ##EL 9 ES EL L1 1001 Y PONE DE ESTADO 0001 QUE ES ESTADO 1 (PRENDIDO$
UNO=True
pulso=1
ledState=False
estadoAnterior=False
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(5,GPIO.OUT) ##GPIO20 como salida
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(12,GPIO.IN)
while True:
        if (not GPIO.input(12)):
                time.sleep(0.06)
                if (not GPIO.input(12)):
                        GPIO.output(5,CERO)
			GPIO.output(6,CERO)
			GPIO.output(13,CERO)
			GPIO.output(19,CERO)
			GPIO.output(22,CERO)
			GPIO.output(27,CERO)
		while(not GPIO.input(12)):
			time.sleep(0.1)

