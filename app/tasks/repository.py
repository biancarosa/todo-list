"""app.tasks.repository

Module that deals saving and retrieving Tasks."""
from app.tasks import models
from app.main import db
class TaskRepository:

    DEFAULT_LIMIT = 50
    
    def save(self, task):
        db.session.add(task)
        db.session.commit()
        return task
    
    def list(self):
        return models.Task.query.limit(self.DEFAULT_LIMIT).all()

