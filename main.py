from app import create_app, db
from flask_restful import Api
from app.resources.task_resource import TaskListResource, TaskResource

app = create_app()

api = Api(app)

# Registrar los recursos y sus rutas
api.add_resource(TaskListResource, '/tasks')
api.add_resource(TaskResource, '/tasks/<int:task_id>')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
