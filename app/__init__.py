from flask import Flask, request, jsonify
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import views


login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()

    
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config["SECRET_KEY"] = 'thisissecretkey'


db.init_app(app)
migrate.init_app(app, db)
login_manager.login_view = 'auth.login'

login_manager.init_app(app)

@app.route('/', methods=['GET'])
def hello():
    return "app is running"

app.register_blueprint(views.admin_routes, url_prefix='/admin')
    

if __name__ == '__main__':
    app.run(debug=True)


