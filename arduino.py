import serial 
import time

try:
    arduino = serial.Serial(port='COM6', baudrate=115200, timeout=0.5)
except Exception:
        print("geen connectie met arduino gevonden")
        

def write(values):
    print(values)
    
    arduino.write((values+"\n").encode("utf-8"))
    print(arduino.readline().decode('utf-8'))
    
   
# while True:
    # time.sleep(1)
    # write("150,0,1,1,0,150")
    # time.sleep(1)
    # write("150,1,0 .,0,1,150")
    