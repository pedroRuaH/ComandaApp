# importar dependencias
from flask import Flask
from config import Config
from models import db
from auth.routes import auth_bp
from main.routes import main_bp
from flask import render_template, redirect, url_for, session

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    @app.route('/', methods=['GET'])
    def home():
        return render_template('home.html')
    
    @app.route('/dashboard')
    def dashboard():
        if not session.get('user_authenticated'):
            return redirect(url_for('auth.login'))
        return render_template('dashboard.html', username=session.get('username'))
    
    @app.route('/JesusDev', methods=['GET'])
    def JesusDev():
        return render_template('JesusDev.html', title='JesusDev Page')

    @app.route('/MarioDev', methods=['GET'])
    def MarioDev():
        return render_template('MarioDev.html', title='MarioDev')
    
    return app
 

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)