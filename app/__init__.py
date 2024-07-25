from flask import Flask, request, jsonify
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy



def make_app():
    
    db = SQLAlchemy()

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    login_manager = LoginManager()

    login_manager.login_view = 'auth.login'

    login_manager.init_app(app)

    @app.route('/', methods=['GET'])
    def hello():
        return "app is running"
    
    return app


