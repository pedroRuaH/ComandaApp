from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return redirect(url_for('index'))

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html', title='Index Page')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html', title='Login')

if __name__ == '__main__':
    app.run(debug=True)
