from flask_restful import Resource
from flask import request
from app import db
from app.models.task import Task


class TaskListResource(Resource):
    def get(self):
        tasks = Task.query.all()
        tasks_list = [{"id": task.id, "title": task.title, "description": task.description, "done": task.done} for task in tasks]
        return {"tasks": tasks_list}, 200

    def post(self):
        data = request.get_json()
        new_task = Task(title=data['title'], description=data['description'], done=data.get('done', False))
        db.session.add(new_task)
        db.session.commit()
        return {"message": "Task created successfully."}, 201

class TaskResource(Resource):
    def get(self, task_id):
        task = Task.query.get_or_404(task_id)
        return {"id": task.id, "title": task.title, "description": task.description, "done": task.done}, 200

    def put(self, task_id):
        task = Task.query.get_or_404(task_id)
        data = request.get_json()
        task.title = data['title']
        task.description = data['description']
        task.done = data['done']
        db.session.commit()
        return {"message": "Task updated successfully."}, 200

    def delete(self, task_id):
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return {"message": "Task deleted successfully."}, 204
