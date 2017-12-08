# coding: UTF-8
import serial
from flask import Flask,render_template
app = Flask(__name__)

def megane1():
    with serial.Serial('COM6',9600) as ser:
        i = b'1'
        ser.write(i)
        ser.close()

def megane2():
    with serial.Serial('COM6',9600) as ser:
        i = b'2'
        ser.write(i)
        ser.close()

def megane3():
    with serial.Serial('COM6',9600) as ser:
        i = b'3'
        ser.write(i)
        ser.close()

@app.route('/')
def index():
    title = "meganeApp"
    return render_template('meganeApp.html',title=title)

    #return "死にたい"



@app.route('/post', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        if '1' in request.form:
            megane1()
        if '2' in request.form:
            meagne2()
        if '3' in request.form:
            megane3()

if __name__ == "__main__":
    app.run()