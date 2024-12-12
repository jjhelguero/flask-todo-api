from datetime import datetime, timezone
import uuid
from typing import List, Optional, Dict, Any

class TodoRepository:
    def __init__(self):
        self.tasks = [
            {
                'id': uuid.UUID('a463a6fe-2f67-4925-9e00-12ee154e58de'),
                'created': datetime.now(timezone.utc),
                'completed': False,
                'task': 'Create Flask API tutorial'
            }
        ]

    def get_all(self) -> List[Dict[str, Any]]:
        return self.tasks

    def create(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        task = {
            'id': uuid.uuid4(),
            'created': datetime.now(timezone.utc),
            'completed': False,
            'task': task_data['task']
        }
        self.tasks.append(task)
        return task

    def get_by_id(self, task_id: uuid.UUID) -> Optional[Dict[str, Any]]:
        return next((task for task in self.tasks if task['id'] == task_id), None)

    def update(self, task_id: uuid.UUID, task_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        task = self.get_by_id(task_id)
        if task:
            task.update({
                'completed': task_data['completed'],
                'task': task_data['task']
            })
        return task

    def delete(self, task_id: uuid.UUID) -> bool:
        for index, task in enumerate(self.tasks):
            if task['id'] == task_id:
                self.tasks.pop(index)
                return True
        return False
