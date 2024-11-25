from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os


class Config(object):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fsdkfd32r234fsdf'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost/academy'

    ################
    # Flask-Security
    ################

    SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
    SECURITY_PASSWORD_SALT = "fsdfdfsdfdfsdafds"


app = Flask(__name__)
app.secret_key = 'some secret salt555'
app.config.from_object(Config)
#app.config.from_pyfile('config-extended.py')
app.app_context().push()

db = SQLAlchemy(app)
migrate = Migrate(app,db)

# runs the app instance
app.app_context().push()

login_manager = LoginManager(app)
login_manager.login_view = 'login'

#Регистрация путей Blueprint
#from start.routes import main_bp
#app.register_blueprint(main_bp, url_prefix="/")


from start import routes, models