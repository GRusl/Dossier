import datetime

import sqlalchemy

from .db_session import SqlAlchemyBase

from werkzeug.security import generate_password_hash, check_password_hash


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True)

    surname = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String)

    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    city = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    description = sqlalchemy.Column(sqlalchemy.Text, nullable=True)

    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    modified_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def __repr__(self):
        return f'<Colonist> {self.id} {self.surname} {self.name}'