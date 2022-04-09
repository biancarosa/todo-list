"""app.tasks.tasks

Module that deals with Tasks route."""
from flask import jsonify, request
from app.tasks import models, repository

tasks_repository = repository.TaskRepository()

def create():
    """Creates tasks."""
    json = request.get_json()
    task = models.Task(json.get('description'))
    tasks_repository.save(task)
    return jsonify(dict(task))

def list():
    """Returns the task list."""
    tasks = tasks_repository.list()
    return jsonify({
        "data": [dict(task) for task in tasks]
    })

def patch():
    """Patches a task, changing the data object 
    only with the data passed on the request.
    Maintains attributes not sent to the API."""
    tasks = []
    for json in request.get_json():
        task = tasks_repository.get(json.get('id'))
        task.status = json.get('status', task.status)
        task.description =  json.get('description', task.description)
        tasks_repository.save(task)
        tasks.append(dict(task))
    return jsonify(tasks)
