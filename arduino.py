import serial 

arduino = serial.Serial(port='COM6', baudrate=115200, timeout=.1)

def write(values):
    
    arduino.write(b'values')
    print(b'values')
    

write("255,0,1,0,1,255")
print(arduino.readline()) 