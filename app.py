from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def MarioDev():
    return render_template('MarioDev.html', title='MarioDev')

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', title='Home Page')
@app.route('/MarioDev', methods=['GET'])
def mario_dev():
    return render_template('MarioDev.html', title='MarioDev')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html', title='Login')

if __name__ == '__main__':
    app.run(debug=True)
    
    