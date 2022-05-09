from data import db_session
from data.user import User

from flask import Blueprint, url_for, jsonify

from flask_restful import Resource, Api, abort

from settings import MainDB

db_session.global_init(MainDB.name)  # Инициализация БД

user_api_blueprint = Blueprint('user_api', __name__)  # Создание приложения
api = Api(user_api_blueprint)  # Инициализация API


def abort_if_user_not_found(user_id):
    db_sess = db_session.create_session()  # Подключение к БД
    user = db_sess.query(User).get(user_id)  # Получение обьекта пользователя
    if not user:  # Проверка на существование обьекта пользователя
        abort(404, message=f"User {user_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)

        db_sess = db_session.create_session()

        user = db_sess.query(User).get(user_id)
        return jsonify(
            {
                'data': user.to_dict(
                    only=('id', 'email', 'example',
                          'surname', 'name', 'age',
                          'city', 'description')
                ),
                'url': url_for('profile:profile', pk=user.id)
            }
        )


class UsersListResource(Resource):
    def get(self):
        db_sess = db_session.create_session()

        users = db_sess.query(User).all()
        return jsonify(
            {
                'users': [
                    item.to_dict(
                        only=('id', 'email')
                    ) for item in users
                ]
            }
        )


api.add_resource(UsersListResource, '')
api.add_resource(UsersResource, '<int:user_id>')
