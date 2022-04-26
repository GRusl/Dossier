from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, NumberRange


class ProfileForm(FlaskForm):
    surname = StringField('Фамилия пользователя')
    name = StringField('Имя пользователя', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[NumberRange(14, 100)])
    city = StringField('Название населенного пункта')
    description = TextAreaField('О себе')
    submit = SubmitField('Сохранить')
