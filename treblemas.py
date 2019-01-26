import smbus
bus = smbus.SMBus(1)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)

def decrementar():
	fichero = open('/usr/lib/python2.7/dist-packages/RPi/treble.txt')
        fichero.seek(0)
        numero = fichero.read()
        fichero.close()
        numero = int(numero) - 1
        bus.write_byte_data(0x44, 0x05, numero)
        numero = str(numero)
        fichero = open('/usr/lib/python2.7/dist-packages/RPi/treble.txt','w')
        fichero.seek(0)
        fichero.write(numero)
        fichero.close()
        fichero = open('/usr/lib/python2.7/dist-packages/RPi/treble.txt')
        numero = fichero.read()
        print(numero)
        fichero.close()

def incrementar():
	fichero = open('/usr/lib/python2.7/dist-packages/RPi/treble.txt')
        fichero.seek(0)
        numero = fichero.read()
        fichero.close()
        numero = int(numero) + 1
        bus.write_byte_data(0x44, 0x05, numero)
        numero = str(numero)
        fichero = open('/usr/lib/python2.7/dist-packages/RPi/treble.txt','w')
        fichero.seek(0)
        fichero.write(numero)
        fichero.close()
        fichero = open('/usr/lib/python2.7/dist-packages/RPi/treble.txt')
        numero = fichero.read()
        print(numero)
        fichero.close()


fichero = open('/usr/lib/python2.7/dist-packages/RPi/treble.txt')
variable = fichero.read()
fichero.seek(0)
fichero.close()
if int(variable)==7:
	fichero = open('/usr/lib/python2.7/dist-packages/RPi/treble.txt',"w")
	fichero.seek(0)
	fichero.write("15")
	fichero.close()
	decrementar()

elif int(variable)>8:
	decrementar()

elif int(variable)<7:
	incrementar()
	
