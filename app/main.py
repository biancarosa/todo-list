"""app.main

Module that starts the Flask application
"""
from flask import Flask

from app.healthcheck import blueprint as health_check_blueprint
from app.tasks import blueprint as tasks_blueprint

# pylint: disable=C0103
app = Flask(__name__)
app.register_blueprint(health_check_blueprint.create_blueprint())
app.register_blueprint(tasks_blueprint.create_blueprint())
