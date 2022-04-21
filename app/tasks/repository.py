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
    
    def bulk_save(self, tasks):
        for task in tasks: 
            db.session.add(task)
        db.session.commit()
        return tasks
    
    def get(self, id):
        return db.session.query(models.Task).get(id)
    
    def list(self):
        return models.Task.query.order_by(models.Task.id.asc()).limit(self.DEFAULT_LIMIT).all()

    def get_many(self, ids):
        return models.Task.query.filter(models.Task.id.in_(ids)).all()