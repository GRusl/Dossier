import os

from flask import Flask, render_template, url_for
from flask_login import LoginManager

from data import db_session

from settings import MainDB

from data.user import User

from apps import entrance, profile, images, publication

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

'''user = User()
user.email = 'test@test.com'
user.surname = 'vssfse'
user.name = 'bhjscchsb'
user.hashed_password = 123
db_sess.add(user)

publication = Publication()
publication.author = 1
publication.title = '1234'
publication.text = 'khbs kscuhbjdcdcusbjcfvyjebvdefguywbvhg3t78fyurbh4g'
db_sess.add(publication)

publication = Publication()
publication.author = 1
publication.title = '45325652413653'
publication.text = 'vdfbjhguivybjhkvhkewfguivybjhergybjhekgvyubjhfuififwhfheifhwufhwiefhueh'
db_sess.add(publication)

db_sess.commit()'''


@login_manager.user_loader
def load_user(user_id):
    return db_sess.query(User).get(user_id)


@app.route('/')
def index():
    return render_template('homepage/homepage.html',
                           title='Главная')


if __name__ == '__main__':
    app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='favicon.ico'))
    app.run()
