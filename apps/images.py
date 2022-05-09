import os

from flask_login import current_user, login_required

from settings import MainDB

from flask import request, abort, redirect, url_for
from flask import Blueprint, render_template

from data import db_session
from data.image import Image

from forms.uploading_img import UploadingImgForm

db_session.global_init(MainDB.name)  # Инициализация БД

images_blueprint = Blueprint('images', __name__)  # Создание приложения


@images_blueprint.route('/')
def index():  # Главная страница со списком изображений
    db_sess = db_session.create_session()  # Подключение к БД

    images = db_sess.query(Image).filter(Image.private == False).all()

    return render_template('images/img_list.html',
                           title='Список изображений',
                           images=images,
                           my_btn=True)


@images_blueprint.route('/my')
@login_required
def my_img():  # Страница со списком изображений пользователя
    db_sess = db_session.create_session()  # Подключение к БД

    images = db_sess.query(Image).filter(Image.user == current_user).all()

    return render_template('images/img_list.html',
                           title='Список моих изображений',
                           images=images,
                           my_btn=False)


@images_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add():  # Добавление изображения
    form = UploadingImgForm()  # Инициализация формы
    if request.method == 'POST' and form.validate_on_submit():  # Проверка запроса на POST
        db_sess = db_session.create_session()  # Подключение к БД

        form.file.data.save(os.path.join('./media/', form.file.data.filename))  # Сохранение изображения

        img = Image()  # Создание изображения
        img.owner = current_user.id
        img.path = form.file.data.filename
        img.description = form.description.data
        img.private = form.private.data
        db_sess.add(img)

        db_sess.commit()  # Применение изменений

        return redirect(url_for('images.index'))  # Перенос на общий список изображений

    return render_template('images/add_img.html',  # Отображение формы
                           title='Добавить изображение',
                           form=form)


@images_blueprint.route('/delete/<int:pk>')
@login_required
def delete(pk):  # Удаление изображения
    db_sess = db_session.create_session()  # Подключение к БД

    # Получение удаляемого обьекта
    image = db_sess.query(Image).filter(Image.id == pk, Image.user == current_user).first()
    if image:  # Проверка на существование объекта
        db_sess.delete(image)  # Удаление
        db_sess.commit()  # Применение изменений
    else:
        abort(404)  # Ошибка 404

    return redirect(url_for('images.my_img'))  # Перенос на изоражения пользователя
