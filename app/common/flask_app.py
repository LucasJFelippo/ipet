from threading import Lock

from typing import List

from flask import Blueprint, Flask
from flask_login import LoginManager


class FlaskAppMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class FlaskApp(metaclass=FlaskAppMeta):
    def __init__(self) -> None:
        self.app = Flask(import_name = __name__, instance_relative_config = True)
        self.app.secret_key = 'dev'

        self.login_manager = LoginManager()
        self.login_manager.init_app(self.app)

        @self.login_manager.user_loader
        def load_user(user_id):
            pass

        self.login_manager.login_view = "Auth.login"


    def register_blueprints(self, blueprints: List[Blueprint]) -> None:
        for b in blueprints:
            self.app.register_blueprint(b)