"""app.healthcheck.blueprint

Module taht deals with Blueprint-related stuff."""
from flask import Blueprint
from app.tasks import tasks, models

def create_blueprint():
    """Creates a Blueprint"""
    blueprint = Blueprint('Tasks Blueprint', __name__, url_prefix='/tasks')
    blueprint.route('/', methods=['POST'])(tasks.create)
    blueprint.route('/', methods=['GET'])(tasks.list)
    return blueprint
