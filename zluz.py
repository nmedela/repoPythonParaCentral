import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#fichero = open('/usr/lib/python2.7/dist-packages/RPi/volumen.txt')
print('empieza')
time.sleep(2.1)
print('termina')
print('empieza')
time.sleep(2.9)
print('termina')
#GPIO.setup(18,GPIO.OUT) ##GPIO18 como salida indica si hay que atenuar
#GPIO.setup(27,GPIO.OUT) ##GPIO27 como salida
#GPIO.setup(22,GPIO.OUT) ##GPIO22 como salida


#GPIO.output(18, not GPIO.input(18))

#if fichero.read() == '0':
#        print('no se puede mas')
#else:
#        fichero.seek(0)
#        numero = fichero.read()
#        fichero.close()
#        numero = int(numero) + 2
#        bus.write_byte_data(0x44, 0x02, numero)
#        numero = str(numero)
#        fichero = open('/usr/lib/python2.7/dist-packages/RPi/volumen.txt','w')
#       fichero.seek(0)
#        fichero.write(numero)
#        fichero.close()
#        fichero = open('/usr/lib/python2.7/dist-packages/RPi/volumen.txt')
#        numero = fichero.read()
#        print(numero)
#        fichero.close()

