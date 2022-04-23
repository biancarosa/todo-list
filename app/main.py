"""app.main

Module that starts the Flask application
"""
import os
import logging
import newrelic.agent

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from app.logger import init_logger

def populate_db():
    from app.tasks import models, repository
    tasks_repository = repository.TaskRepository()
    for i in range(0,15000):
        task = models.Task(f"Task {i}")
        tasks_repository.save(task)

def handle_bad_request(e):
    return jsonify({"error": "BadRequest"}), 400
    
def handle_internal_server_error(e):
    return jsonify({"error": "InternalServerError"}), 500


newrelic.agent.initialize()
newrelic.agent.register_application()

# pylint: disable=C0103
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:////tmp/test.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from app.healthcheck import blueprint as health_check_blueprint
from app.tasks import blueprint as tasks_blueprint

app.register_blueprint(health_check_blueprint.create_blueprint())
app.register_blueprint(tasks_blueprint.create_blueprint())

app.register_error_handler(400, handle_bad_request)
app.register_error_handler(500, handle_internal_server_error)

init_logger()
logger = logging.getLogger(__name__)

try:
    logger.info('Creating db schema.')
    db.create_all()
    populate_db()
except Exception as e:
    logger.error(e)


