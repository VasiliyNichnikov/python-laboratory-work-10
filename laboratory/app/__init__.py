from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Создание приложение
app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

# Инициализация БД
db = SQLAlchemy(app)

# Подключение таблиц
from app.page.pharmacy import Pharmacy

# Создание БД
with app.test_request_context():
    db.create_all()


# Подключение blueprints
import app.page.controller as page
from app.page import restapi

app.register_blueprint(page.module)
app.register_blueprint(restapi.module)

# Логи
if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler

    file_handler = RotatingFileHandler("tmp/myblog.log", 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info("MyBlog startup")
