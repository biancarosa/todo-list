"""app.tasks.models

Module that deals with Tasks models."""
from app.main import db
class Task(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    description = db.Column(db.String)

    def __init__(self, description):
        self.description = description
    
    def __iter__(self):
        yield 'description', self.description
