from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def MarioDev():
    return render_template('MarioDev.html', title='MarioDev')

@app.route('/home', methods=['GET'])
def home():

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html', title='Login')

if __name__ == '__main__':
    app.run(debug=True)
