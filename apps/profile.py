from data import db_session

from data.user import User
from data.publication import Publication

from forms.add_publication import AddPublicationForm

from flask import Blueprint, render_template

db_session.global_init('./db/test1.sqlite')
db_sess = db_session.create_session()

profile_blueprint = Blueprint('profile', __name__)


@profile_blueprint.route('/<int:pk>')
def profile(pk):
    return render_template('profile/profile.html',
                           title='Посмотреть досье',
                           publications=db_sess.query(Publication).filter(Publication.author == pk))


@profile_blueprint.route('/add', methods=['GET', 'POST'])
def add_publication():
    form = AddPublicationForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()

        publication = Publication()
        publication.author = 1
        publication.img_id = form.img_id.data
        publication.title = form.title.data
        publication.text = form.text.data
        db_sess.add(publication)

        db_sess.commit()

        return 'ok'

    return render_template('profile/add_publication.html',
                           title='Посмотреть досье',
                           form=form)


@profile_blueprint.route('/edit')
def edit():
    return 'Редактировать'
