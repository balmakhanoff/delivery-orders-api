from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # Конфигурация базы данных
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///delivery_service.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Импортируем маршруты
    from .routes import api_bp
    app.register_blueprint(api_bp)

    # Создаем все таблицы
    with app.app_context():
        db.create_all()

    return app
