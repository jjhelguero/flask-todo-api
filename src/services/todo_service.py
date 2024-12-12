from typing import Dict, List, Any
import uuid
from src.repositories.todo_repository import TodoRepository

class TodoService:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def get_tasks(self, order_by: str, order: str) -> List[Dict[str, Any]]:
        tasks = self.repository.get_all()
        return sorted(
            tasks,
            key=lambda task: task[order_by],
            reverse=order == 'desc'
        )

    def create_task(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        return self.repository.create(task_data)

    def get_task(self, task_id: uuid.UUID) -> Dict[str, Any]:
        task = self.repository.get_by_id(task_id)
        if not task:
            raise KeyError(f'Task with ID {task_id} not found.')
        return task

    def update_task(self, task_id: uuid.UUID, task_data: Dict[str, Any]) -> Dict[str, Any]:
        task = self.repository.update(task_id, task_data)
        if not task:
            raise KeyError(f'Task with ID {task_id} not found.')
        return task

    def delete_task(self, task_id: uuid.UUID) -> None:
        if not self.repository.delete(task_id):
            raise KeyError(f'Task with ID {task_id} not found.')
