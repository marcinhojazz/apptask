from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from db import db
from resources import TaskResource, TaskListResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db.init_app(app)
api = Api(app)
CORS(app)  # Habilita CORS para todas as rotas

# Garante que as tabelas sejam criadas antes do primeiro pedido
with app.app_context():
    db.create_all()

api.add_resource(TaskListResource, '/tasks')
api.add_resource(TaskResource, '/tasks/<int:task_id>')

if __name__ == '__main__':
    app.run(debug=True)
