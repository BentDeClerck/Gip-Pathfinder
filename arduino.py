import serial 
import time

arduino = serial.Serial(port='COM6', baudrate=115200, timeout=1)

def write(values):
    
    arduino.write((values+"\n").encode("utf-8"))
    time.sleep(0)
    print(arduino.readline().decode('utf-8'))
    
while True:
    time.sleep(1)
    write("255,0,1,0,1,255")
    time.sleep(1)
    write("255,1,0,1,0,255")
    