from flask_wtf import FlaskForm

from wtforms import SubmitField, BooleanField, FileField, TextAreaField
from wtforms.validators import DataRequired


class LoadingImgForm(FlaskForm):
    file = FileField('Изображение', validators=[DataRequired()])

    description = TextAreaField('Image Description')

    private = BooleanField('Приватное')
    submit = SubmitField('Войти')
