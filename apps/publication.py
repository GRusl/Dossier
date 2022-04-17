from settings import MainDB

from flask import request, Blueprint, render_template, redirect, abort

from data import db_session
from data.publication import Publication

from forms.loading_publication import LoadingPublicationForm

db_session.global_init(MainDB.name)
db_sess = db_session.create_session()

publication_blueprint = Blueprint('publication', __name__)


@publication_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = LoadingPublicationForm()
    if request.method == 'POST' and form.validate_on_submit():
        db_sess = db_session.create_session()

        publication = Publication()
        publication.author = 1
        publication.img_id = form.img_id.data
        publication.title = form.title.data
        publication.text = form.text.data
        db_sess.add(publication)

        db_sess.commit()

        return redirect('/profile/1')

    return render_template('publication/add_publication.html',
                           title='Посмотреть досье',
                           form=form)


@publication_blueprint.route('/delete/<int:pk>', methods=['GET', 'POST'])
def delete(pk):
    publication = db_sess.query(Publication).filter(Publication.id == pk).first()
    if publication:
        db_sess.delete(publication)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/profile/1')
