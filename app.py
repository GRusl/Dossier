import os

from flask import Flask

from data import db_session

from data.user import User
from data.publication import Publication

from apps import entrance, profile, images

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'secret_key')
app.config['DEBUG'] = os.environ.get('DEBUG', False)

app.register_blueprint(entrance.entrance_blueprint, url_prefix='/entrance')
app.register_blueprint(profile.profile_blueprint, url_prefix='/profile')
app.register_blueprint(images.images_blueprint, url_prefix='/images')

db_session.global_init('./db/test1.sqlite')
db_sess = db_session.create_session()

'''user = User()
user.email = 'test@test.com'
user.surname = 'vssfse'
user.name = 'bhjscchsb'
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

for publication in db_sess.query(Publication).filter(Publication.author == 1):
    print(publication)


@app.route('/')
def index():
    return 'Главная'


if __name__ == '__main__':
    app.run()
