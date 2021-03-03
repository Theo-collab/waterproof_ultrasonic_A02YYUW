import serial
from time import sleep

ser = serial.Serial (port='/dev/ttyS0', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=1)

def measure():
    received_data = ser.read()              #read serial port
    sleep(0.01)
    data_left = ser.inWaiting()             #check for remaining byte
    received_data += ser.read(data_left)
    data = received_data
    if data[0]==255:
        distance = data[1]*256 + data[2]
        return distance
