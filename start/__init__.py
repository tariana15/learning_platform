from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
from flask_admin.menu import MenuLink
from werkzeug.security import generate_password_hash
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


from start.routes import MyAdminIndexView
class UserAdmin(ModelView):
    column_list = ('id', 'username', 'email', 'roles','active')
    form_columns = ('username', 'email', 'roles')
    
    # Удалим form_args и изменим способ настройки отношения
    column_auto_select_related = True
    
    # Настройка отображения связей
    form_excluded_columns = ('password',)  # если есть такое поле

    def on_model_change(self, form, model, is_created):
        """
        Этот метод вызывается перед сохранением модели
        """
        if is_created:
            # Только для новых пользователей устанавливаем пароль по умолчанию
            model.password = generate_password_hash('default_password')

    
    # Настройка отношения roles
    form_widget_args = {
        'roles': {
            'data-role': 'select2'  # использование select2 для удобного выбора
        }
    }

class RoleAdmin(ModelView):
# Исправляем списки отображаемых и редактируемых полей
    column_list = ['id', 'name']  # используем списки вместо кортежей
    form_columns = ['name']       # только поле name для формы
    
    def __init__(self, *args, **kwargs):
        super(RoleAdmin, self).__init__(*args, **kwargs)


# Инициализация админки
admin = Admin(app, name='Admin', template_mode='bootstrap4',index_view=MyAdminIndexView())

# Добавьте эту строку в конфигурацию
app.config['FLASK_ADMIN_SWATCH'] = 'cosmo'

from start.models import User, Role
from start.routes import ChangePasswordView, LogoutView
# Добавляем views
admin.add_view(UserAdmin(User, db.session, name='Пользователи'))
admin.add_view(RoleAdmin(Role, db.session, name='Роли'))
admin.add_view(ChangePasswordView(name='Изменить пароль', endpoint='change_password'))
admin.add_view(LogoutView(name='Выход', endpoint='admin_logout'))

from start import routes, models