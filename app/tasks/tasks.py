"""app.tasks.tasks

Module that deals with Tasks route."""
from flask import jsonify
from app.tasks import models, repository

tasks_repository = repository.TaskRepository()

def create():
    """Creates tasks."""
    json = request.get_json()
    task = models.Task(json.get('description'))
    tasks_repository.save(task)
    return jsonify(task)

def list():
    """Returns the task list."""
    tasks = tasks_repository.list()
    return jsonify({
        "data": [dict(task) for task in tasks]
    })
