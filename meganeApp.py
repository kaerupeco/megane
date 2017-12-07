# coding: UTF-8
import serial
from flask import Flask
app = Flask(__name__)

def main():
    with serial.Serial('COM6',9600) as ser:
        i = b'1'
        print(i)

        ser.write(i)
        ser.close()

if __name__ == "__main__":
    main()