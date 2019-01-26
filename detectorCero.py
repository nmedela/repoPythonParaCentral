from thread import start_new_thread
import os, time, sys
import RPi.GPIO as GPIO
import time
import socket
CERO=True
UNO=False
pulso=0.005
nuevo=0.005
aux=0.005
#pipe_name = 'pipe_test'
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26,GPIO.IN) #GPIO26 como entrada
GPIO.setup(19,GPIO.OUT)
GPIO.output(19,False)   #GPIO17 enciend
#s=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
#s.bind(("",9999))
#s.listen(1)
#sc, addr = s.accept()
#def PasoCero(channel):
#	global pulso
#	global nuevo
#	if not ( nuevo == pulso):
#		if (nuevo >  pulso):
#			 pulso += 0.00001
#		else:
#			 pulso -= 0.00001
#	time.sleep(pulso)
#	GPIO.output(19,True) #lo prendo por un rato
#	GPIO.output(19,False) #lo apago
#Interrupciones
#GPIO.add_event_detect(26, GPIO.FALLING, callback = PasoCero) #detecta el pin como interrupcion de pas opor cero
#Bucle principal
def principal(a):
	global aux
	global nuevo
	while( True ):
		#pipein = open(pipe_name, 'r')
		#nuevo = float(pipein.readline())
#		while (not GPIO.input(26)):
		GPIO.wait_for_edge(26,GPIO.FALLING)
		if (aux < 0.01):
			if (aux < nuevo ):
				aux += 0.00001
			if (aux > nuevo):
				aux -= 0.00001
			time.sleep(aux)
        		GPIO.output(19,True) #lo prendo por un rato
			time.sleep(0.00001)
       			GPIO.output(19,False) #lo apago

def secundario(a):
	global nuevo
#	global sc
#	global s
	s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
	s.bind(("",9999))
	s.listen(1)
	sc, addr = s.accept()
	while( True ):
		recibido = sc.recv(1024)
		nuevo=float(recibido)
		sc.send(recibido)
		recibido=""
		sc.close()
		sc, addr = s.accept()
#		print( aux )
#		time.sleep(1)
#		aux-=0.0001


start_new_thread(principal,(1,))
#start_new_thread(secundario,(1,))
while ( True ):
	time.sleep(10)
