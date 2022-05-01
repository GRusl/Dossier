import os

from flask_login import current_user, login_required

from settings import MainDB

from flask import request, abort, redirect, url_for
from flask import Blueprint, render_template

from data import db_session
from data.image import Image

from forms.uploading_img import UploadingImgForm

db_session.global_init(MainDB.name)
db_sess = db_session.create_session()

images_blueprint = Blueprint('images', __name__)


@images_blueprint.route('/')
def index():
    return render_template('images/img_list.html',
                           title='Список изображений',
                           images=db_sess.query(Image).filter(Image.private == False),
                           my_btn=True)


@images_blueprint.route('/my')
@login_required
def my_img():
    return render_template('images/img_list.html',
                           title='Список моих изображений',
                           images=db_sess.query(Image).filter(Image.private == False, Image.user == current_user),
                           my_btn=False)


@images_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = UploadingImgForm()
    if request.method == 'POST' and form.validate_on_submit():
        db_sess = db_session.create_session()

        form.file.data.save(os.path.join('./media/', form.file.data.filename))

        img = Image()
        img.owner = current_user.id
        img.path = form.file.data.filename
        img.description = form.description.data
        img.private = form.private.data
        db_sess.add(img)

        db_sess.commit()

        return redirect(url_for('images.index'))

    return render_template('images/add_img.html',
                           title='Добавить изображение',
                           form=form)


@images_blueprint.route('/delete/<int:pk>')
@login_required
def delete(pk):
    image = db_sess.query(Image).filter(Image.id == pk, Image.user == current_user).first()
    if image:
        db_sess.delete(image)
        db_sess.commit()
    else:
        abort(404)

    return redirect(url_for('images.my_img'))
