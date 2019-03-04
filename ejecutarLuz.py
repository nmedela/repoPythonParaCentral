import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT) ##GPIO18 como salida bit 2 de la codificacion indica las etapas 1010
GPIO.setup(27,GPIO.OUT) ##GPIO27 como salida bit 1 de la codificacion
GPIO.setup(22,GPIO.OUT) ##GPIO22 como salida bit 0 de la codificacion
luz=0
informacion=[0,0,0,0,0,0,0,0] #aca se almacenan los datos de los parametros para recorrerlos  enviarlos
GPIO.output(18, False)


def enviarBitAPuerto(puerto , estado):
        if (estado == '0'):
                GPIO.output(puerto, False)
        else:
                GPIO.output(puerto, True)


def formatearParametros():
	i=0
	luz = '{0:02b}'.format(int(sys.argv[1]))
#	print(luz)
	for bit in str(luz):
		informacion[i]=bit
		i = i + 1

	intensidad = '{0:06b}'.format(int(sys.argv[2]))
	print(intensidad)
	for bit in str(intensidad):
        	informacion[i]= bit
		i = i + 1
	print(informacion)

formatearParametros()
h=0
while( h <8):
	enviarBitAPuerto(27,informacion[h])
	print(informacion[h])
	h= h + 1
	enviarBitAPuerto(22,informacion[h])
	print(informacion[h])
	h = h + 1
	time.sleep(0.08)
	GPIO.output(18, not GPIO.input(18))
	print(" ")
	print(GPIO.input(18))
	print(" ")
	time.sleep(0.08)

GPIO.output(22, False)
GPIO.output(27, False)
GPIO.output(18, False)
time.sleep(0.5)
