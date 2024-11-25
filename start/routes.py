from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_user, login_required, current_user, logout_user

from start import app
from start.models import db, User, login_manager, Role
from werkzeug.security import generate_password_hash, check_password_hash


#main_bp = Blueprint('main_blueprint', __name__)
@app.route("/courses")
# @login_required
def courses():
    return render_template("courses.html", user=current_user)


@app.route("/cours_1")
# @login_required
def cours_1():
    return render_template("cours_1.html")


@app.route("/cours_2")
@login_required
def cours_2():
    return render_template("cours_2.html")


@app.route("/cours_3")
@login_required
def cours_3():
    return render_template("cours_3.html")


@app.route('/', methods=['GET', 'POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username and password:
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)

            next_page = request.args.get('next')

            return redirect('courses')
        else:
            flash('Имя пользователя или Пароль не корректен')
    else:
        flash('Пожалуйста заполните поля Имя пользователя и Пароль')
    return render_template('login.html')


@app.route('/registration', methods=['GET', 'POST'] )
def registration():
    name = request.form.get('name')
    role = request.form.getlist('role')
    email = request.form.get('e-mail')
    username = request.form.get('username')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    if request.method == 'POST':
        if not (name or role or email or username or password or password2):
            flash ('Пожалуйста заполните все поля')
        elif password != password2:
            flash('Пароли не совпадают')
        else:
            hash_pwd = generate_password_hash(password)
            new_user = User(name=name,email=email,username=username,password=hash_pwd, active=1)
            # store the role
            role = Role.query.filter_by(id=request.form['role']).first()
            new_user.roles.append(role)

            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
    return render_template('registration.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route('/layout')
# @login_required
def layout():
    return render_template('layout.html', user=current_user.username)

@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)