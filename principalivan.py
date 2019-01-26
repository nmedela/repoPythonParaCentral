import RPi.GPIO as GPIO
import time
CERO=True ##EL 9 ES EL L1 1001 Y PONE DE ESTADO 0010 QUE ES ESTADO 2 (PRENDIDO A MEDIO FULL)
UNO=False
pulso=0.1
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(20, GPIO.IN) ##GPIO20 como entrada para el detector de paso por cero
GPIO.setup(5,GPIO.OUT) ##GPIO5 como salida L1
GPIO.setup(6,GPIO.OUT) ##GPIO6 como salida L2
GPIO.setup(13,GPIO.OUT) ##GPIO13 como salida L3
GPIO.setup(19,GPIO.OUT) ##GPIO19 como salida L$


def CuentaB(channel):
    global contaB
    contaB += 1
    os.system("clear")
    print "Contador B: ", contaB

#Interrupciones
GPIO.add_event_detect(20, GPIO.RISING, callback = CuentaB)


GPIO.output(5, UNO)
GPIO.output(6, CERO)
GPIO.output(13,CERO)
GPIO.output(19, UNO) ## PRIMERO SELECCIONO LA LUZ
time.sleep(pulso)

while (contaB<5):
	pass
