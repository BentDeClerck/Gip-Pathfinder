import serial 
import time

try:
    arduino = serial.Serial(port='COM3', baudrate=115200, timeout=0.5)
except Exception:
        print("geen connectie met arduino gevonden")
        

def write(values):
    
    
    arduino.write((values+"\n").encode("utf-8"))
    print(arduino.readline().decode('utf-8'))
    



time.sleep(2)
write("321321")
