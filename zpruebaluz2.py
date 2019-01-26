import RPi.GPIO as GPIO
import time
CERO=False ##EL 9 ES EL L1 1001 Y PONE DE ESTADO 0001 QUE ES ESTADO 1 (PRENDIDO$
UNO=True
pulso=1
ledState=False
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(6,GPIO.OUT) ##GPIO6 como salida
GPIO.setup(20,GPIO.IN)
estadoAnterior=GPIO.input(20)
GPIO.output(6,CERO)
while True:
        if (not GPIO.input(20) == estadoAnterior):
                time.sleep(0.06)
                if (not GPIO.input(20) == estadoAnterior):
                        ledState = not ledState
                        estadoAnterior= not estadoAnterior
                        GPIO.output(6,not GPIO.input(6))

