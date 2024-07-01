from flask_restful import Resource, reqparse
from models import Task
from db import db

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, required=True, help='Title of the task')
parser.add_argument('completed', type=bool)

class TaskResource(Resource):
    def get(self, task_id):
        task = Task.query.get_or_404(task_id)
        return {'id': task.id, 'title': task.title, 'completed': task.completed}

    def put(self, task_id):
        args = parser.parse_args()
        task = Task.query.get_or_404(task_id)
        task.title = args['title']
        task.completed = args['completed']
        db.session.commit()
        return {'id': task.id, 'title': task.title, 'completed': task.completed}

    def delete(self, task_id):
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return '', 204

class TaskListResource(Resource):
    def get(self):
        tasks = Task.query.all()
        return [{'id': task.id, 'title': task.title, 'completed': task.completed} for task in tasks]

    def post(self):
        args = parser.parse_args()
        task = Task(title=args['title'], completed=args['completed'])
        db.session.add(task)
        db.session.commit()
        return {'id': task.id, 'title': task.title, 'completed': task.completed}, 201
