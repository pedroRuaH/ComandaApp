# importar dependencias
from flask import Flask
from config import Config
from src.models import db
from routes.auth.routes import auth_bp
from routes.main.routes import main_bp
from routes.inventory.routes import inventory_bp
from flask import render_template, redirect, url_for, session

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(inventory_bp)
    from src.api.products import blueprint as products_bp

    app.register_blueprint(products_bp, url_prefix="/products")


    @app.route('/', methods=['GET'])
    def home():
        return render_template('home.html')
    
    @app.route('/dashboard')
    def dashboard():
        if not session.get('user_authenticated'):
            return redirect(url_for('auth.login'))
        return render_template('dashboard.html', username=session.get('username'))
    
    @app.route('/inventory', methods=['GET'])
    def inventory():
        return render_template('inventory.html', title='inventory')

    @app.route('/jesus_profile', methods=['GET'])
    def jesus_profile():
        return render_template('profiles/jesus_profile.html', title='JesusDev Page')

    @app.route('/mario_profile', methods=['GET'])
    def mario_profile():
        return render_template('profiles/mario_profile.html', title='MarioDev')

    @app.route('/pedro_profile', methods=['GET'])
    def pedro_profile():
        return render_template('profiles/pedro_profile.html', title='Pedro Profile')
    
    @app.route('/rafa_profile', methods=['GET'])
    def rafa_profile():
        return render_template('profiles/rafa_profile.html', title='Rafa Profile')


    return app
 

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)