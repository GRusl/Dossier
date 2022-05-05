from data import db_session
from data.user import User

from flask import Blueprint, redirect, render_template, request, url_for

from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from forms.login import LoginForm
from forms.registration import RegisterForm

from settings import MainDB

db_session.global_init(MainDB.name)  # Инициализация БД
db_sess = db_session.create_session()  # Подключение к БД

entrance_blueprint = Blueprint('entrance', __name__)  # Создание приложения

login_manager = LoginManager()  # Создание объекта регистрации
login_manager.init_app(entrance_blueprint, add_context_processor=False)  # Регистрация объекта регистрации


@login_manager.user_loader
def load_user(user_id):
    return db_sess.query(User).get(user_id)


@entrance_blueprint.route('/login', methods=['GET', 'POST'])
def login():  # Вход пользователя
    form = LoginForm()  # Инициализация формы
    if request.method == 'POST' and form.validate_on_submit():  # Проверка запроса на POST
        user = db_sess.query(User).filter(User.email == form.email.data).first()  # Получение объекта пользователя

        if user and user.check_password(form.password.data):  # Проверка корректности введенных данных
            login_user(user, remember=form.remember_me.data)  # Авторизация
            return redirect(url_for('profile.profile', pk=current_user.id))  # Переход в профиль
        return render_template('entrance/login.html',  # Возвращение сообщения об ошибке
                               message='Неправильный логин или пароль',
                               form=form)
    return render_template('entrance/login.html', title='Авторизация', form=form)  # Отображение формы авторизации


@entrance_blueprint.route('/logout')
@login_required
def logout():  # Выход
    logout_user()  # Выход из аккаунта
    return redirect(url_for('entrance.login'))  # Перенос на поле авторизации


@entrance_blueprint.route('/registration', methods=['GET', 'POST'])
def registration():  # Регистрация
    form = RegisterForm()  # Инициализация формы
    message = None
    if request.method == 'POST' and form.validate_on_submit():  # Проверка запроса на POST
        if form.password.data == form.password_again.data:
            user = User()  # Создание пользователя
            user.email = form.email.data
            user.set_password(form.password.data)
            user.surname = form.surname.data
            user.name = form.name.data
            db_sess.add(user)

            db_sess.commit()  # Применение изменений

            return redirect(url_for('entrance.login'))  # Перенос на поле авторизации
        else:
            message = 'Пароли не совпадают...'

    return render_template('entrance/registration.html',  # Отображение формы
                           title='Регистарция',
                           form=form,
                           message=message)
