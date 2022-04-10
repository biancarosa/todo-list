"""app.main

Module that starts the Flask application
"""
import os
import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.logger import init_logger

init_logger()
logger = logging.getLogger(__name__)

# pylint: disable=C0103
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:////tmp/test.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app.healthcheck import blueprint as health_check_blueprint
from app.tasks import blueprint as tasks_blueprint

app.register_blueprint(health_check_blueprint.create_blueprint())
app.register_blueprint(tasks_blueprint.create_blueprint())


try:
    logger.info('Creating db schema.')
    db.create_all()
except:
    logger.info('Schema created already. Skipping.')
