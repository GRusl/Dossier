import os

from flask import Flask

from apps import entrance, profile, images

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'secret_key')
app.config['DEBUG'] = os.environ.get('DEBUG', False)

app.register_blueprint(entrance.entrance_blueprint, url_prefix='/entrance')
app.register_blueprint(profile.profile_blueprint, url_prefix='/profile')
app.register_blueprint(images.images_blueprint, url_prefix='/images')


@app.route('/')
def index():
    return 'Главная'


@app.route('/<int:user_id>')
def read(user_id):
    return f'Просмотреть досье {user_id}'


if __name__ == '__main__':
    app.run()
