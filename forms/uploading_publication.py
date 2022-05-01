from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired


class UploadingPublicationForm(FlaskForm):
    img_id = IntegerField('id изображения')

    title = StringField('Заголовок', validators=[DataRequired()])
    text = TextAreaField('Содержание', validators=[DataRequired()])

    submit = SubmitField('Сохранить')
