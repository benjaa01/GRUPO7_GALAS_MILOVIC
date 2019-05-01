import serial
ser = serial.Serial('/dev/ttyACM0',9600)
s=[0]
n=0;
numeros = []
archivo = open("PruebaGuardar.txt","w")
while (n<=32000):
	read_serial=ser.readline()
	#s[0]=str(int(ser.readline(),16))
	#print s[0]
	print read_serial
	numeros.append(read_serial)
	n=n+1 
largo = len(numeros);
for i in range(largo):
	archivo.write('%s\n'%numeros[i])	
archivo.close()


