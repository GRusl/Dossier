from data import db_session
from data.user import User

from flask import Blueprint, redirect, render_template

from flask_login import LoginManager, login_user

from forms.login import LoginForm

entrance_blueprint = Blueprint('entrance', __name__)

login_manager = LoginManager()
login_manager.init_app(entrance_blueprint, add_context_processor=False)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@entrance_blueprint.route('/', methods=['GET', 'POST'])
@entrance_blueprint.route('/entrance', methods=['GET', 'POST'])
def entrance():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()

        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('entrance/login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('entrance/login.html', title='Авторизация', form=form)


@entrance_blueprint.route('/registration')
def registration():
    return 'Регистрация'


@entrance_blueprint.route('/recovery')
def recovery():
    return 'Востановление'
