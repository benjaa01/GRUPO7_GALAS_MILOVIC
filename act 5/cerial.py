import serial
ser = serial.Serial('/dev/ttyAMA0', 9600)
mensaje= 'some text'
ser.write(mensaje.encode())
while True:
	print(ser.read())
