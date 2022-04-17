from settings import MainDB

from flask import request, Blueprint, render_template, redirect

from data import db_session
from data.publication import Publication

from forms.loading_publication import LoadingPublicationForm

db_session.global_init(MainDB.name)
db_sess = db_session.create_session()

profile_blueprint = Blueprint('profile', __name__)


@profile_blueprint.route('/<int:pk>')
def profile(pk):
    return render_template('profile/profile.html',
                           title='Посмотреть досье',
                           publications=db_sess.query(Publication).filter(Publication.author == pk))


@profile_blueprint.route('/edit')
def edit():
    return 'Редактировать'
