from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def hello():
    #return name
    #return render_template('index.html', title='flask test', name=name) #変更
    return render_template('index.html')

## おまじない
if __name__ == "__main__":
    app.run(debug=True)