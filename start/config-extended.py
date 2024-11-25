##########
# Features
##########

SQLALCHEMY_TRACK_MODIFICATIONS = False


################
# Flask-Security
# https://pythonhosted.org/Flask-Security/configuration.html
################

# URLs
SECURITY_URL_PREFIX = "/admin"
SECURITY_POST_LOGIN_VIEW = "/admin/"
SECURITY_POST_LOGOUT_VIEW = "/admin/"
SECURITY_POST_REGISTER_VIEW = "/admin/"

# Включает регистрацию
SECURITY_REGISTERABLE = True
SECURITY_REGISTER_URL = "/registration"
SECURITY_SEND_REGISTER_EMAIL = False

# Включет сброс пароля
SECURITY_RECOVERABLE = True
SECURITY_RESET_URL = "/reset/"
SECURITY_SEND_PASSWORD_RESET_EMAIL = True

# Включает изменение пароля
SECURITY_CHANGEABLE = True
SECURITY_CHANGE_URL = "/change/"
SECURITY_SEND_PASSWORD_CHANGE_EMAIL  = False

# todo не работает отправка email
# AttributeError: 'NoneType' object has no attribute 'send'