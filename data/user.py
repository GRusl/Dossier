import datetime

import sqlalchemy
from flask_login import UserMixin

from data.db_session import SqlAlchemyBase

from werkzeug.security import generate_password_hash, check_password_hash


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True)

    example = sqlalchemy.Column(sqlalchemy.Boolean, default=False)

    surname = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String)

    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    city = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    description = sqlalchemy.Column(sqlalchemy.Text, nullable=True)

    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def __repr__(self):
        return f'<Colonist> {self.id} {self.surname} {self.name}'
