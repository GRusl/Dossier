import os

from flask import Flask, render_template, send_from_directory
from flask_login import LoginManager

from apps import entrance, profile, images, publication

from data import db_session
from data.user import User

from settings import MainDB

from waitress import serve

app = Flask(__name__)  # Создание приложения
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'secret_key')  # Настройка секретного ключа
app.config['DEBUG'] = os.environ.get('DEBUG', False)  # Установка режима тестирования
app.config['UPLOAD_FOLDER'] = {'png', 'jpg'}  # Установка формата загружаемых файлов

login_manager = LoginManager()  # Создание объекта регистрации
login_manager.init_app(app)  # Регистрация объекта регистрации

# Регистрация приложений
app.register_blueprint(publication.publication_blueprint, url_prefix='/publication')  # Работа с публикациями
app.register_blueprint(entrance.entrance_blueprint, url_prefix='/entrance')  # Обработка входа на страницу
app.register_blueprint(profile.profile_blueprint, url_prefix='/profile')  # Работа с профилем
app.register_blueprint(images.images_blueprint, url_prefix='/images')  # Работа с изображениями

db_session.global_init(MainDB.name)  # Инициализация БД
db_sess = db_session.create_session()  # Подключение к БД


@login_manager.user_loader
def load_user(user_id):
    return db_sess.query(User).get(user_id)


@app.route('/media/<filename>')
def media(filename):  # Обработка выдачи media
    return send_from_directory('./media/', filename)


@app.route('/')
def index():  # Главная страница
    examples = db_sess.query(User).filter(User.example == True)

    return render_template('homepage/homepage.html',
                           title='Главная',
                           examples=examples)


if __name__ == '__main__':  # Запуск сервера
    serve(app, host='0.0.0.0', port=5000)
