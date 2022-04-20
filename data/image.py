import datetime

import sqlalchemy
from flask import url_for
from sqlalchemy import orm

from data.db_session import SqlAlchemyBase


class Image(SqlAlchemyBase):
    __tablename__ = 'images'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    path = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True)

    owner = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    user = orm.relation('User')

    description = sqlalchemy.Column(sqlalchemy.Text)

    private = sqlalchemy.Column(sqlalchemy.BOOLEAN)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)

    def get_url(self):
        return url_for('static', filename=f'img/uploaded/{self.path}')

    def __repr__(self):
        return f'<Image> {self.id} {self.path}'
