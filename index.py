import serial
import requests
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def hello():
    #return name
    #return render_template('index.html', title='flask test', name=name) #変更
    return render_template('hello.html')

@app.route('/sendtext',methods=['POST'])
def sendMeganeMode():

    return(request.form['megane'])
    #return request.post('/hello.html')
    
app.run(debug=True)