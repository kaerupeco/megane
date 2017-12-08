from flask import Flask
import serial
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    # webサーバー立ち上げ
    app.run()