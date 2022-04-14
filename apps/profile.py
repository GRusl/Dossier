from data import db_session

from data.user import User
from data.publication import Publication

from flask import Blueprint, render_template

db_session.global_init('./db/test1.sqlite')
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
