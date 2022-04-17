from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired


class LoginPublicationForm(FlaskForm):
    img_id = IntegerField('id изображения', validators=[DataRequired()])

    title = StringField('Заголовок', validators=[DataRequired()])
    text = TextAreaField('Содержание', validators=[DataRequired()])

    submit = SubmitField('Сохранить')
