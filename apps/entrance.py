from data import db_session
from data.user import User

from flask import Blueprint, redirect, render_template, request, url_for

from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from forms.login import LoginForm
from forms.registration import RegisterForm

from settings import MainDB

db_session.global_init(MainDB.name)
db_sess = db_session.create_session()

entrance_blueprint = Blueprint('entrance', __name__)

login_manager = LoginManager()
login_manager.init_app(entrance_blueprint, add_context_processor=False)


@login_manager.user_loader
def load_user(user_id):
    return db_sess.query(User).get(user_id)


@entrance_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = db_sess.query(User).filter(User.email == form.email.data).first()

        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('profile.profile', pk=current_user.id))
        return render_template('entrance/login.html',
                               message='Неправильный логин или пароль',
                               form=form)
    return render_template('entrance/login.html', title='Авторизация', form=form)


@entrance_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('entrance.login'))


@entrance_blueprint.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User()
        user.email = form.email.data
        user.set_password(form.password.data)
        user.surname = form.surname.data
        user.name = form.name.data
        db_sess.add(user)

        db_sess.commit()

        return redirect(url_for('entrance.login'))

    return render_template('entrance/registration.html',
                           title='Регистарция',
                           form=form)


@entrance_blueprint.route('/recovery')
def recovery():
    return 'Востановление'
