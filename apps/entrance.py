from flask import Blueprint

entrance_blueprint = Blueprint('entrance', __name__)


@entrance_blueprint.route('/')
@entrance_blueprint.route('/entrance')
def entrance():
    return 'Вход'


@entrance_blueprint.route('/registration')
def registration():
    return 'Регистрация'


@entrance_blueprint.route('/recovery')
def recovery():
    return 'Востановление'
