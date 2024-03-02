from flask import Flask
from src.routers.home import home
from src.routers.auth import auth
from src.routers.user import user
from src.routers.tours import tours
from src.routers.reserves import reserve
from config import DATABASE_CONNECTION_URI, Config
from src.utils.db import db


def app_create():
    app = Flask(__name__)

    print(DATABASE_CONNECTION_URI)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
    app.config.from_object(Config)

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    app.register_blueprint(home)
    app.register_blueprint(auth)
    app.register_blueprint(user)
    app.register_blueprint(tours)
    app.register_blueprint(reserve)

    return app