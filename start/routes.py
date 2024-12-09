from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from flask_login import login_user, login_required, current_user, logout_user

from start import app
from start.models import db, User, login_manager, Role, Result, check_previous_results, save_results, TeacherStudent, final_result_available
from werkzeug.security import generate_password_hash, check_password_hash


#main_bp = Blueprint('main_blueprint', __name__)
@app.route("/courses")
# @login_required
def courses():
    return render_template("courses.html", user=current_user)


@app.route("/cours_1", methods=['GET', 'POST'])
# @login_required
def cours_1():
    if request.method == 'POST':
        data = request.get_json()
        answers = data['answers']
        user_id = current_user.id
        test_number = 1
        # Сохранение результатов в БД
        save_results(user_id, test_number, answers)
        return jsonify(success=True)
    
    results_available = check_previous_results(current_user.id)
    return render_template("cours_1.html", results_available=results_available)


@app.route("/cours_2", methods=['GET', 'POST'])
@login_required
def cours_2():
    if request.method == 'POST':
        data = request.get_json()
        answers = data['answers']
        user_id = current_user.id
        test_number = 2
        # Сохранение результатов в БД
        save_results(user_id, test_number, answers)
        return jsonify(success=True)
    
    results_available = check_previous_results(current_user.id)
    return render_template("cours_2.html", results_available=results_available)


@app.route("/cours_3", methods=['GET', 'POST'])
@login_required
def cours_3():
    if request.method == 'POST':
        data = request.get_json()
        answers = data['answers']
        user_id = current_user.id
        test_number = 3
        # Сохранение результатов в БД
        save_results(user_id, test_number, answers)
        return jsonify(success=True)
    
    results_available = check_previous_results(current_user.id)
    return render_template("cours_3.html", results_available=results_available)


@app.route('/', methods=['GET', 'POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username and password:
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            # request.args.get('next')
            return redirect('courses')
        else:
            flash('Имя пользователя или Пароль не корректен')
    else:
        flash('Пожалуйста заполните поля Имя пользователя и Пароль')
    return render_template('login.html')


@app.route('/registration', methods=['GET', 'POST'] )
def registration():
    name = request.form.get('name')
    # role = request.form.getlist('role')
    email = request.form.get('e-mail')
    username = request.form.get('username')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    if request.method == 'POST':
        if not (name or email or username or password or password2):
            flash ('Пожалуйста заполните все поля')
        elif password != password2:
            flash('Пароли не совпадают')
        else:
            hash_pwd = generate_password_hash(password)
            new_user = User(name=name,email=email,username=username,password=hash_pwd, active=1)
            # store the role
            # role = Role.query.filter_by(id=request.form['role']).first()
            # new_user.roles.append(role)

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

@app.route('/final_test', methods=['GET', 'POST'])
def final_test():
    if request.method == 'POST':
        data = request.get_json()
        answers = data['answers']
        user_id = current_user.id
        test_number = 4
        # Сохранение результатов в БД
        save_results(user_id, test_number, answers)
        return jsonify(success=True)
    
    # Проверка доступности теста
    results_available = check_previous_results(current_user.id)
    final_finished = final_result_available(current_user.id)
    # print(current_user.roles[0].name)
    return render_template('final_test.html', results_available=results_available, final_finished=final_finished)

@app.route('/teacher')
@login_required
def teacher():
    if current_user.has_role('student'): # Проверка, что роль - ученик
        flash('У вас нет доступа к этой странице.')
        return redirect('/')  # Перенаправление на главную страницу

    # Получение информации о текущем пользователе
    user_info = {
        'name': current_user.username,
        'email': current_user.email
    }

    # Получение student_id для учеников, привязанных к этому учителю
    student_ids = db.session.query(TeacherStudent).filter_by(teacher_id=current_user.id).all()
    student_ids = [student_id[0] for student_id in student_ids]  # Преобразование кортежей в список

    # Получение результатов тестов учеников
    students_results = Result.query.filter(Result.student_id.in_(student_ids)).all()

    return render_template('teacher.html', user_info=user_info, students_results=students_results)