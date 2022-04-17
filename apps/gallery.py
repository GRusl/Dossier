import os

from settings import MainDB

from flask import request
from flask import Blueprint, render_template

from data import db_session
from data.user import User
from data.image import Image

from forms.loading_img import LoadingImgForm

db_session.global_init(MainDB.name)
db_sess = db_session.create_session()

gallery_blueprint = Blueprint('gallery', __name__)


@gallery_blueprint.route('/')
def gallery():
    return 'Список изображений'


@gallery_blueprint.route('/add', methods=['GET', 'POST'])
def add_img():
    form = LoadingImgForm()
    if request.method == 'POST' and form.validate_on_submit():
        db_sess = db_session.create_session()

        form.file.data.save(os.path.join('./static/img/uploaded/',
                                         form.file.data.filename))

        img = Image()
        img.owner = 1
        img.path = form.file.data.filename
        img.description = form.description.data
        img.private = form.private.data
        db_sess.add(img)

        # db_sess.commit()

        return 'ok'

    return render_template('gallery/add_img.html',
                           title='Добавить изображение',
                           form=form)
