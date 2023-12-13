from doctest import debug
import importlib
import os

from flask import blueprints
from typing import List

from app.common.flask_app import FlaskApp
from app.config import features_with_blueprint


def get_blueprints(name_List) -> List:
    blueprint_list = []
    for name in name_List:
        m = importlib.import_module("app." + name + "." + name)
        b = m.__dict__[name]
        blueprint_list.append(b)
    return blueprint_list


def main() -> None:
    flaskApp = FlaskApp()
    flaskApp.register_blueprints(get_blueprints(features_with_blueprint))

    flaskApp.app.run(debug=True)