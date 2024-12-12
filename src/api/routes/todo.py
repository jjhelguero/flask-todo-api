from flask.views import MethodView
from flask_smorest import Blueprint, abort
from src.api.schemas.todo import (
    CreateTask, UpdateTask, Task, ListTasks, ListTasksParameters
)
from src.services.todo_service import TodoService
from src.repositories.todo_repository import TodoRepository

todo = Blueprint('todo', 'todo', url_prefix='/todo', description='Todo API')
todo_service = TodoService(TodoRepository())

@todo.route('/tasks')
class TodoCollection(MethodView):
    @todo.arguments(ListTasksParameters, location='query')
    @todo.response(status_code=200, schema=ListTasks)
    def get(self, parameters):
        try:
            return {'tasks': todo_service.get_tasks(
                parameters['order_by'].value,
                parameters['order'].value
            )}
        except Exception as e:
            abort(500, str(e))

    @todo.arguments(CreateTask)
    @todo.response(status_code=201, schema=Task)
    def post(self, task_data):
        try:
            return todo_service.create_task(task_data)
        except Exception as e:
            abort(500, str(e))

@todo.route('/tasks/<uuid:task_id>')
class TodoTask(MethodView):
    @todo.response(status_code=200, schema=Task)
    def get(self, task_id):
        try:
            return todo_service.get_task(task_id)
        except KeyError as e:
            abort(404, str(e))
        except Exception as e:
            abort(500, str(e))

    @todo.arguments(UpdateTask)
    @todo.response(status_code=200, schema=Task)
    def put(self, payload, task_id):
        try:
            return todo_service.update_task(task_id, payload)
        except KeyError as e:
            abort(404, str(e))
        except Exception as e:
            abort(500, str(e))

    @todo.response(status_code=204)
    def delete(self, task_id):
        try:
            todo_service.delete_task(task_id)
        except KeyError as e:
            abort(404, str(e))
        except Exception as e:
            abort(500, str(e))
