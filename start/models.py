from datetime import datetime

from flask import redirect
from flask_login import UserMixin
from flask_security import RoleMixin
from start import db, login_manager, app
from werkzeug.security import generate_password_hash, check_password_hash


roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('roles.id'))
)

class TeacherStudent(db.Model):
    __tablename__ = 'teachers_students'  # Имя таблицы в базе данных

    teacher_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True, nullable=False)  # Внешний ключ на таблицу пользователей (учителей)
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True, nullable=False)  # Внешний ключ на таблицу пользователей (учеников)

    # Определение отношений
    teacher = db.relationship('User', foreign_keys=[teacher_id], backref='teacher_students')
    student = db.relationship('User', foreign_keys=[student_id], backref='student_teachers')

    def __repr__(self):
        return f'<TeacherStudent {self.teacher_id} - {self.student_id}>'

class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
    # Нужен для security!
    active = db.Column(db.Boolean())
    # Для получения доступа к связанным объектам
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

    # Flask - Login
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    # Flask-Security
    def has_role(self, *args):
        return set(args).issubset({role.name for role in self.roles})

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.username

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Result(db.Model):
    __tablename__ = 'results'
    student_id = db.Column(db.Integer, nullable=False)
    student_result = db.Column(db.String, nullable=False)  # Строка из 0 и 1
    test_number = db.Column(db.Integer, nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    


def save_results(user_id, test_number, answers):
    """Сохраняет результаты теста в базе данных."""
    new_result = Result(student_id=user_id, test_number=test_number, student_result=answers)
    db.session.add(new_result)
    db.session.commit()


def check_previous_results(user_id):
    """Проверяет, прошел ли пользователь предыдущие тесты."""
    final_ready = 0
    results1 = Result.query.filter(Result.student_id == user_id, Result.test_number == 1).all()
    if len(results1) > 0:
        final_ready += 1
    results2 = Result.query.filter(Result.student_id == user_id, Result.test_number == 2).all()
    if len(results2) > 0:
        final_ready += 1
    results3 = Result.query.filter(Result.student_id == user_id, Result.test_number == 3).all()
    if len(results3) > 0:
        final_ready += 1
    return final_ready == 3  # Проверяем, что есть результаты для трех тестов


def final_result_available(user_id):
    """Проверяет, прошел ли пользователь предыдущие тесты."""
    results = Result.query.filter(Result.student_id == user_id, Result.test_number == 4).all()
    return len(results) != 1  # Проверяем, что есть результаты для итогового теста