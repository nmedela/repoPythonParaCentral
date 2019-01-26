import smbus

bus = smbus.SMBus(1)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)

DEVICE_ADDRESS = 0x44     #7 bit address (despues se le agrega el bit de escritura y lectura)
DEVICE_REG_INPUT=0x00
DEVICE_REG_GAIN = 0x01
DEVICE_REG_VOLUMEN = 0x02
DEVICE_REG_BASS = 0x04
DEVICE_REG_TREBLE = 0x05
DEVICE_REG_SPEAKER_R = 0x06
DEVICE_REG_SPEAKER_L= 0x07
#Write a single register
fichero = open("/usr/lib/python2.7/dist-packages/RPi/volumen.txt")
valor= int(fichero.read())
fichero.close()
fichero = open("/usr/lib/python2.7/dist-packages/RPi/mute.txt")
estado= fichero.read()
fichero.close()
if estado=="no":
	bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_VOLUMEN, 56)
	fichero=open("/usr/lib/python2.7/dist-packages/RPi/mute.txt","w")
	fichero.seek(0)
	fichero.write("si")
	fichero.close()
else:
	fichero=open("/usr/lib/python2.7/dist-packages/RPi/mute.txt","w")
        fichero.seek(0) 
        fichero.write("no")
        fichero.close()
	bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_VOLUMEN, valor)
