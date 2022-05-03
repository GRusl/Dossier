import os

from flask import Flask, render_template, send_from_directory
from flask_login import LoginManager

from apps import entrance, profile, images, publication

from data import db_session
from data.user import User

from settings import MainDB

from waitress import serve

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'secret_key')
app.config['DEBUG'] = os.environ.get('DEBUG', False)
app.config['UPLOAD_FOLDER'] = {'png', 'jpg'}

login_manager = LoginManager()
login_manager.init_app(app)

app.register_blueprint(publication.publication_blueprint, url_prefix='/publication')
app.register_blueprint(entrance.entrance_blueprint, url_prefix='/entrance')
app.register_blueprint(profile.profile_blueprint, url_prefix='/profile')
app.register_blueprint(images.images_blueprint, url_prefix='/images')

db_session.global_init(MainDB.name)
db_sess = db_session.create_session()


@login_manager.user_loader
def load_user(user_id):
    return db_sess.query(User).get(user_id)


@app.route('/media/<filename>')
def media(filename):
    return send_from_directory('./media/', filename)


@app.route('/')
def index():
    examples = db_sess.query(User).filter(User.example == True)
    print(examples)

    return render_template('homepage/homepage.html',
                           title='Главная',
                           examples=examples)


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
