from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed

from wtforms import SubmitField, BooleanField, FileField, TextAreaField
from wtforms.validators import DataRequired


class LoadingImgForm(FlaskForm):
    file = FileField(
        'Изображение',
        validators=[
            DataRequired(),
            FileAllowed(['jpg', 'png'], 'Только .jpg или .png')
        ]
    )

    description = TextAreaField('Image Description')

    private = BooleanField('Приватное')
    submit = SubmitField('Загрузить')