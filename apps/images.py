from flask import Blueprint

images_blueprint = Blueprint('images', __name__)


@images_blueprint.route('/')
def index():
    return 'Просмотреть доступные картинки'


@images_blueprint.route('/add')
def add():
    return 'Добавить'
