import serial
import requests
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/sendtext',methods=['POST'])
def sendMeganeMode():
    meganeMode = request.form['megane']
    encoded_meganeMode = meganeMode.encode(encoding='utf-8')
    with serial.Serial('COM6',9600) as ser:
        #return(i)
        ser.write(encoded_meganeMode)
        ser.close()
        return encoded_meganeMode

app.run(app, host='0.0.0.0', port=8000)