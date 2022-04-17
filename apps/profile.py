from settings import MainDB

from flask import request, Blueprint, render_template

from data import db_session
from data.publication import Publication

from forms.login_publication import LoginPublicationForm

db_session.global_init(MainDB.name)
db_sess = db_session.create_session()

profile_blueprint = Blueprint('profile', __name__)


@profile_blueprint.route('/<int:pk>')
def profile(pk):
    return render_template('profile/profile.html',
                           title='Посмотреть досье',
                           publications=db_sess.query(Publication).filter(Publication.author == pk))


@profile_blueprint.route('/add', methods=['GET', 'POST'])
def add_publication():
    form = LoginPublicationForm()
    if request.method == 'POST' and form.validate_on_submit():
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
