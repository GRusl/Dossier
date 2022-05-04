from flask_login import current_user, login_required

from settings import MainDB

from flask import request, Blueprint, render_template, redirect, abort, url_for

from data import db_session
from data.publication import Publication
from data.image import Image

from forms.uploading_publication import UploadingPublicationForm

db_session.global_init(MainDB.name)  # Инициализация БД
db_sess = db_session.create_session()  # Подключение к БД

publication_blueprint = Blueprint('publication', __name__)  # Создание приложения


@publication_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add():  # Добавление публикации
    message = ''
    form = UploadingPublicationForm()  # Инициализация формы
    if request.method == 'POST' and form.validate_on_submit():  # Проверка запроса на POST
        img = db_sess.query(Image).get(form.img_id.data)  # Получение обьекта изображения
        if img:  # Проверка на существование обьекта
            if not img.private or (img.private and img.owner == current_user.id):  # Проверка на доступность изображения
                publication = Publication()  # Создание публикации
                publication.author = current_user.id
                publication.img_id = form.img_id.data
                publication.title = form.title.data
                publication.text = form.text.data
                db_sess.add(publication)

                db_sess.commit()  # Применение изменений

                return redirect(url_for('profile.profile', pk=current_user.id))  # Перенос в профиль
            else:
                message = 'Автор изображения запретил использовать его другим пользователям'
        else:
            message = 'Нельзя использовать несуществующее изображение'

    return render_template('publication/add_publication.html',  # Отображение формы
                           title='Посмотреть досье',
                           form=form,
                           message=message)


@publication_blueprint.route('/delete/<int:pk>', methods=['GET', 'POST'])
@login_required
def delete(pk):  # Удаление
    # Получение удаляемого обьекта
    publication = db_sess.query(Publication).filter(Publication.id == pk, Publication.user == current_user).first()
    if publication:  # Проверка на существование
        db_sess.delete(publication)  # Удаление
        db_sess.commit()  # Применение изменений
    else:
        abort(404)  # Ошибка 404
    return redirect(url_for('profile.profile', pk=current_user.id))  # Перенос в профиль


@publication_blueprint.route('/edit/<int:pk>', methods=['GET', 'POST'])
@login_required
def edit(pk):  # Редактирование
    form = UploadingPublicationForm()  # Инициализация формы
    publication = db_sess.query(Publication).filter(Publication.id == pk).first()
    if request.method == 'GET':  # Обработка GET запроса
        if publication:  # Проверка на существование
            # Внесение имеющихся значений в поля
            form.img_id.data = publication.img_id
            form.title.data = publication.title
            form.text.data = publication.text
        else:
            abort(404)  # Ошибка 404
    elif request.method == 'POST' and form.validate_on_submit():  # Обработка Post запроса
        if publication:  # Проверка на существование
            # Замена на новые значения
            publication.img_id = form.img_id.data
            publication.title = form.title.data
            publication.text = form.text.data
            db_sess.commit()  # Применение изменений
            return redirect(url_for('profile.profile', pk=current_user.id))  # Перенос в профиль
        else:
            abort(404)  # Ошибка 404

    return render_template('publication/add_publication.html',  # Отображение формы
                           title='Редактирование публикации',
                           form=form)
