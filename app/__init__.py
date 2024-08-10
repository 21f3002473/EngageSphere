from flask import Flask, request, jsonify
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.views import AllViews

from .routes.admin_routes import admin_routes

class EngageSphere:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
        self.app.config["SECRET_KEY"] = 'thisissecretkey'
        self.db = SQLAlchemy(self.app)
        self.migrate = Migrate(self.app, self.db)
        self.login_manager = LoginManager(self.app)
        self.login_manager.login_view = 'auth.login'
        self.login_manager.login_message_category = 'info'

        self.views = AllViews(self.app)
        self.register_routes()

    def register_routes(self):
        self.app.route('/', methods=['GET'])(self.hello)
        self.app.route('/login', methods=['GET'])(self.login)


    def hello(self):
        return "app is running"
    def login(self):
        return "login route is working fine"


if __name__ == '__main__':
    app = EngageSphere().app
    app.run(debug=True)
