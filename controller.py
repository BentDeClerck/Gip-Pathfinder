import pynput; from pynput import keyboard; from pynput.keyboard import Listener, Key, Controller
import time
import serial 

arduino = serial.Serial(port='COM6', baudrate=115200, timeout=0.01)

        

def write(values):  
    arduino.write((values+"\n").encode("utf-8"))
    # print(arduino.readline().decode('utf-8'))
prestate = False

def on_press(key):
    try:
        if key.char == "z" and prestate == False:
            write("150,0,1,1,0,150")
            prestate == True
        if key.char == "s" and prestate == False:
            write("150,1,0,0,1,150")
            prestate == True
        if key.char == "q" and prestate == False:
            write("150,0,1,0,1,150")
            prestate == True
        if key.char == "d" and prestate == False:
            write("150,1,0,1,0,150")  
            prestate == True
    except AttributeError:
        pass
    # time.sleep(0.1)

def on_release(key):
    try:
        
        write("0,0,0,0,0,0")
        if key.char == "z" and prestate == True:
            write("0,0,0,0,0,0")
            prestate == False
        if key.char == "s" and prestate == True:
            write("0,0,0,0,0,0")
            prestate == False
        if key.char == "q" and prestate == True:
            write("0,0,0,0,0,0")
            prestate == False
        if key.char == "d" and prestate == True:
           write("0,0,0,0,0,0")
           prestate == False
        # print('{0} released'.format(key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    except AttributeError:    
        pass

while True:
    write("0,0,0,0,0,0")

    # Collect events until released
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
        # time.sleep(0.1)

    # ...or, in a non-blocking fashion:
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

