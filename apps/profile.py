from flask import Blueprint

profile_blueprint = Blueprint('profile', __name__)


@profile_blueprint.route('/')
def profile():
    return 'Просмотреть профиль'


@profile_blueprint.route('/edit')
def edit():
    return 'Редактировать'
