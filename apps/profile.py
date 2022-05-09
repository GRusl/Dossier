from flask_login import login_required, current_user

from forms.profile import ProfileForm

from settings import MainDB

from flask import Blueprint, render_template, request, abort, redirect, url_for

from data import db_session
from data.user import User
from data.publication import Publication

db_session.global_init(MainDB.name)  # Инициализация БД

profile_blueprint = Blueprint('profile', __name__)  # Создание приложения


@profile_blueprint.route('/<int:pk>')
def profile(pk):  # Отображение профиля
    db_sess = db_session.create_session()  # Подключение к БД

    user = db_sess.query(User).get(pk)
    publications = db_sess.query(Publication).filter(Publication.author == pk).all()

    return render_template('profile/profile.html',
                           title='Посмотреть досье',
                           user=user,
                           publications=publications)


@profile_blueprint.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():  # Редактирование пользователя
    db_sess = db_session.create_session()  # Подключение к БД

    form = ProfileForm()  # Инициализация формы
    user = db_sess.query(User).get(current_user.id)  # Получение обьекта пользователя
    if user:  # Проверка на существование пользователя
        if request.method == 'GET':  # Обработка GET запроса
            # Внесение имеющихся значений в поля
            form.surname.data = user.surname
            form.name.data = user.name
            form.email.data = user.email
            form.age.data = user.age
            form.city.data = user.city
            form.description.data = user.description
        elif request.method == 'POST' and form.validate_on_submit():  # Обработка Post запроса
            # Замена на новые значения
            user.surname = form.surname.data
            user.name = form.name.data
            user.email = form.email.data
            user.age = form.age.data
            user.city = form.city.data
            user.description = form.description.data
            db_sess.commit()  # Применение изменений
            return redirect(url_for('profile.profile', pk=current_user.id))  # Перенос на просмотр профиля
    else:
        abort(404)  # Ошибка 404

    return render_template('profile/edit.html',  # Отображение формы
                           title='Редактировать',
                           form=form)
