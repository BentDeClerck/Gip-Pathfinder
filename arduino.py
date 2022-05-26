import serial 
import time

try:
    arduino = serial.Serial(port='COM3', baudrate=115200, timeout=0.5)
    time.sleep(2) # Even wachten voor goede connectie
except Exception:
        print("geen connectie met arduino gevonden")
        
def write(values):
    arduino.write((values+"\n").encode("utf-8")) # Write array naar arduino 
    print(arduino.readline().decode('utf-8'))
    



write("33")
# 1 = rechtdoor; 2 = naarachter; 3 = draaien rechts 