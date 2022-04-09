"""app.main

Module that starts the Flask application
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# pylint: disable=C0103
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:////tmp/test.db")
db = SQLAlchemy(app)

from app.healthcheck import blueprint as health_check_blueprint
from app.tasks import blueprint as tasks_blueprint



app.register_blueprint(health_check_blueprint.create_blueprint())
app.register_blueprint(tasks_blueprint.create_blueprint())

try:
    db.create_all()
except:
    print('Schema created already. Skipping.')