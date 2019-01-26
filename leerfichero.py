fichero = open('volumen.txt')
if fichero.read() == '0':
	print('no se puede mas')
else:
	fichero.seek(0)
	numero = fichero.read()
	fichero.close()
	numero = int(numero) - 1
	numero = str(numero)
	fichero = open('volumen.txt','w')
	fichero.seek(0)
	fichero.write(numero)
	fichero.close()
	fichero = open('volumen.txt')
	numero = fichero.read()
	print(numero)
	fichero.close()

