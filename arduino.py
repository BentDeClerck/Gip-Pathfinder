import pyfirmata2; from pyfirmata2 import Arduino, util; 
import serial

board = Arduino(Arduino.AUTODETECT)
it = pyfirmata2.util.Iterator(board)
sleeptime = 2

it.start()

def RunArduino():
    print("ok")

RunArduino()