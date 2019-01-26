import RPi.GPIO as GPIO
import time
CERO=True
UNO=False
pulso=0.000677
dato = [0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1]
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT) ##GPIO21 como salida

x=0
GPIO.output(21, CERO)
time.sleep(0.00907)
GPIO.output(21, UNO)
time.sleep(0.0042)

for x in range(0,len(dato)):
        if dato[x]==0:
                GPIO.output(21, CERO)
                time.sleep(0.000550)
        else:
                GPIO.output(21, UNO)
                time.sleep(0.000400)



