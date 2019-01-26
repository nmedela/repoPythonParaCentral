import smbus
bus = smbus.SMBus(1)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)

fichero = open('/usr/lib/python2.7/dist-packages/RPi/volumen.txt')
if fichero.read() == '0':
	print('no se puede mas')
else:
	fichero.seek(0)
	numero = fichero.read()
	fichero.close()
	numero = int(numero) - 2
	bus.write_byte_data(0x44, 0x02, numero)
	numero = str(numero)
	fichero = open('/usr/lib/python2.7/dist-packages/RPi/volumen.txt','w')
	fichero.seek(0)
	fichero.write(numero)
	fichero.close()
	fichero = open('/usr/lib/python2.7/dist-packages/RPi/volumen.txt')
	numero = fichero.read()
	print(numero)
	fichero.close()
