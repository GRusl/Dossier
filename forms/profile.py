from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, NumberRange


class ProfileForm(FlaskForm):
    surname = StringField('Фамилия пользователя', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired(), NumberRange(14, 100)])
    city = StringField('Название населенного пункта', validators=[DataRequired()])
    description = TextAreaField('О себе', validators=[DataRequired()])
    submit = SubmitField('Сохранить')
