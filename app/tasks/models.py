"""app.tasks.models

Module that deals with Tasks models."""
import enum

from app.main import db

class TaskStatus(enum.Enum):
    TO_DO = 1
    DOING = 2
    DONE = 3

class Task(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    description = db.Column(db.String)
    status = db.Column(db.Enum(TaskStatus), default=TaskStatus.TO_DO)

    def __init__(self, description):
        self.description = description
    
    def __iter__(self):
        yield 'description', self.description
