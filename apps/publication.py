from flask_login import current_user, login_required

from settings import MainDB

from flask import request, Blueprint, render_template, redirect, abort

from data import db_session
from data.publication import Publication

from forms.loading_publication import LoadingPublicationForm

db_session.global_init(MainDB.name)
db_sess = db_session.create_session()

publication_blueprint = Blueprint('publication', __name__)


@publication_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = LoadingPublicationForm()
    if request.method == 'POST' and form.validate_on_submit():
        publication = Publication()
        publication.author = current_user.id
        publication.img_id = form.img_id.data
        publication.title = form.title.data
        publication.text = form.text.data
        db_sess.add(publication)

        db_sess.commit()

        return redirect(f'/profile/{current_user.id}')

    return render_template('publication/add_publication.html',
                           title='Посмотреть досье',
                           form=form)


@publication_blueprint.route('/delete/<int:pk>', methods=['GET', 'POST'])
@login_required
def delete(pk):
    publication = db_sess.query(Publication).filter(Publication.id == pk, Publication.user == current_user).first()
    if publication:
        db_sess.delete(publication)
        db_sess.commit()
    else:
        abort(404)
    return redirect(f'/profile/{current_user.id}')


@publication_blueprint.route('/edit/<int:pk>', methods=['GET', 'POST'])
@login_required
def edit(pk):
    form = LoadingPublicationForm()
    if request.method == 'GET':
        publication = db_sess.query(Publication).filter(Publication.id == pk).first()
        if publication:
            form.img_id.data = publication.img_id
            form.title.data = publication.title
            form.text.data = publication.text
        else:
            abort(404)

    if request.method == 'POST' and form.validate_on_submit():
        publication = db_sess.query(Publication).filter(Publication.id == pk).first()
        if publication:
            publication.img_id = form.img_id.data
            publication.title = form.title.data
            publication.text = form.text.data
            db_sess.commit()
            return redirect(f'/profile/{current_user.id}')
        else:
            abort(404)

    return render_template('publication/add_publication.html',
                           title='Редактирование публикации',
                           form=form)
