import RPi.GPIO as GPIO
import time
CERO=False ##EL 9 ES EL L1 1001 Y PONE DE ESTADO 0001 QUE ES ESTADO 1 (PRENDIDO $
UNO=True
pulso=1
ledState=False
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(5,GPIO.OUT) ##GPIO20 como salida
GPIO.setup(21,GPIO.IN)
estadoAnterior=GPIO.input(21)
GPIO.output(5,CERO)
while True:
	if (not GPIO.input(21) == estadoAnterior):
		time.sleep(0.06)
		if (not GPIO.input(21) == estadoAnterior):
			ledState = not ledState
			estadoAnterior= not estadoAnterior
       			GPIO.output(5,not GPIO.input(5))
