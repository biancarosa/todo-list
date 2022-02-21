"""app.tasks.models

Module that deals with Tasks models."""
class Task:
    def __init__(self, description):
        self.description = description
    
    def __iter__(self):
        yield 'description', self.description
