import serial
import socket

TCP_host = '127.0.0.1'
TCP_port = 55551

COM_port = 'COM5'
COM_baudrate= 9600

sentences = ['RSA','THS','VDM','VTG']

def filter(data):
    if data[3:6].decode() in sentences:
        COM.write(data)
        print(data)

TCP = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
TCP.bind(('',TCP_port))
TCP.listen(1)
connection,address = TCP.accept()

COM = serial.Serial(COM_port, COM_baudrate)

while True:
    data = connection.recv(1024)
    filter(data)