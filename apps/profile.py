from flask_login import login_required, current_user

from forms.profile import ProfileForm

from settings import MainDB

from flask import Blueprint, render_template, request, abort, redirect

from data import db_session
from data.user import User
from data.publication import Publication

db_session.global_init(MainDB.name)
db_sess = db_session.create_session()

profile_blueprint = Blueprint('profile', __name__)


@profile_blueprint.route('/<int:pk>')
def profile(pk):
    return render_template('profile/profile.html',
                           title='Посмотреть досье',
                           user=db_sess.query(User).get(pk),
                           publications=db_sess.query(Publication).filter(Publication.author == pk))


@profile_blueprint.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = ProfileForm()
    user = db_sess.query(User).get(current_user.id)
    if user:
        if request.method == 'GET':
            form.surname.data = user.surname
            form.name.data = user.name
            form.email.data = user.email
            form.age.data = user.age
            form.city.data = user.city
            form.description.data = user.description
        elif request.method == 'POST' and form.validate_on_submit():
            user.surname = form.surname.data
            user.name = form.name.data
            user.email = form.email.data
            user.age = form.age.data
            user.city = form.city.data
            user.description = form.description.data
            db_sess.commit()
            return redirect(f'/profile/{current_user.id}')
    else:
        abort(404)

    return render_template('profile/edit.html',
                           title='Редактировать',
                           form=form)
