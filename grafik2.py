
import serial
import os
os.system("dmesg")
print("Band =  ")
bant = int(input())
os.system("clear")
while True:
    port = serial.Serial("/dev/ttyUSB0", baudrate=bant)
    data = port.readline()

    print data
