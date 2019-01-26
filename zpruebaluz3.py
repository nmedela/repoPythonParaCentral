import RPi.GPIO as GPIO
import time
CERO=False ##EL 9 ES EL L1 1001 Y PONE DE ESTADO 0001 QUE ES ESTADO 1 (PRENDIDO$
UNO=True
pulso=1
ledState=False
estadoAnterior=False
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(13,GPIO.OUT) ##GPIO20 como salida
GPIO.setup(19,GPIO.OUT)
GPIO.setup(16,GPIO.IN)
estadoAnterior=GPIO.input(16)
GPIO.output(13,CERO)
GPIO.output(19,CERO)
while True:
        if (not GPIO.input(16) == estadoAnterior):
                time.sleep(0.06)
                if (not GPIO.input(16) == estadoAnterior):
                        ledState = not ledState
                        estadoAnterior= not estadoAnterior
                        GPIO.output(13,not GPIO.input(13))
			GPIO.output(19, not GPIO.input(19))
