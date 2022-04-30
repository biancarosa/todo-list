"""app.tasks.tasks

Module that deals with Tasks route."""
import logging

from flask import jsonify, request
from app.tasks import models, repository

tasks_repository = repository.TaskRepository()
logger = logging.getLogger(__name__)

def create():
    """Creates tasks."""
    try:
        json = request.get_json()
        task = models.Task(json.get('description'))
        tasks_repository.save(task)
        return jsonify(dict(task))
    except:
        raise Exception("Could not create task")

def list():
    """Returns the task list."""
    tasks = tasks_repository.list()
    logger.info(f"Found {len(tasks)} tasks")
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
        logger.info(f"Updating task {task.id}")
        task.status = json.get('status', task.status)
        task.description =  json.get('description', task.description)
        tasks.append(task)
    tasks_repository.bulk_save(tasks)
    return jsonify([dict(task) for task in tasks])
