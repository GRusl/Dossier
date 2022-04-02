import datetime

import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Publication(SqlAlchemyBase):
    __tablename__ = 'publications'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    author = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    user = orm.relation('User')

    img_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("images.id"), nullable=True)
    image = orm.relation('Image')

    text = sqlalchemy.Column(sqlalchemy.Text)

    modified_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return f'<Publication> {self.id} {self.user.name}'
