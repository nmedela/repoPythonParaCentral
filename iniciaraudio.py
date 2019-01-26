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

fichero = open("/usr/lib/python2.7/dist-packages/RPi/volumen.txt","w")
fichero.seek(0)
fichero.write("31")
fichero.close()
fichero = open("/usr/lib/python2.7/dist-packages/RPi/ganancia.txt","w")
fichero.seek(0)
fichero.write("0")
fichero.close()
fichero = open("/usr/lib/python2.7/dist-packages/RPi/bass.txt","w")
fichero.seek(0)
fichero.write("7")
fichero.close()
fichero = open("/usr/lib/python2.7/dist-packages/RPi/treble.txt","w")
fichero.seek(0)
fichero.write("10")
fichero.close()
fichero = open("/usr/lib/python2.7/dist-packages/RPi/derecha.txt","w")
fichero.seek(0)
fichero.write("0")
fichero.close()
fichero = open("/usr/lib/python2.7/dist-packages/RPi/izquierda.txt","w")
fichero.seek(0)
fichero.write("0")
fichero.close()

#Write a single register
bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_INPUT, 0x02)
bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_GAIN, 0x00)
bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_VOLUMEN, 0x1f)
bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_BASS, 0x07)
bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_TREBLE, 0x0a)
bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_SPEAKER_R, 0x00)
bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_SPEAKER_L, 0x00)

