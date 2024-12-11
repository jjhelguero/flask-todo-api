import uuid
from datetime import datetime

def test_get_tasks_empty(client):
    """Test getting tasks list"""
    response = client.get('/todo/tasks')
    assert response.status_code == 200
    data = response.get_json()
    assert 'tasks' in data
    assert isinstance(data['tasks'], list)

def test_create_task(client, sample_task):
    """Test creating a new task"""
    response = client.post('/todo/tasks', json=sample_task)
    assert response.status_code == 201
    data = response.get_json()
    assert data['task'] == sample_task['task']
    assert 'id' in data
    assert 'created' in data
    assert data['completed'] is False

def test_get_task(client, sample_task):
    """Test getting a specific task"""
    # First create a task
    response = client.post('/todo/tasks', json=sample_task)
    task_id = response.get_json()['id']
    
    # Then get it by ID
    response = client.get(f'/todo/tasks/{task_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['task'] == sample_task['task']

def test_update_task(client, sample_task):
    """Test updating a task"""
    # First create a task
    response = client.post('/todo/tasks', json=sample_task)
    task_id = response.get_json()['id']
    
    # Update it
    updated_task = {
        "task": "Updated task",
        "completed": True
    }
    response = client.put(f'/todo/tasks/{task_id}', json=updated_task)
    assert response.status_code == 200
    data = response.get_json()
    assert data['task'] == updated_task['task']
    assert data['completed'] == updated_task['completed']

def test_delete_task(client, sample_task):
    """Test deleting a task"""
    # First create a task
    response = client.post('/todo/tasks', json=sample_task)
    task_id = response.get_json()['id']
    
    # Delete it
    response = client.delete(f'/todo/tasks/{task_id}')
    assert response.status_code == 204
    
    # Verify it's gone
    response = client.get(f'/todo/tasks/{task_id}')
    assert response.status_code == 404

def test_task_not_found(client):
    """Test handling of non-existent task ID"""
    random_id = str(uuid.uuid4())
    response = client.get(f'/todo/tasks/{random_id}')
    assert response.status_code == 404

def test_sort_tasks(client, sample_task):
    """Test task sorting"""
    # Create two tasks
    task1 = {"task": "A task"}
    task2 = {"task": "B task"}
    client.post('/todo/tasks', json=task1)
    client.post('/todo/tasks', json=task2)
    
    # Test ascending sort by task
    response = client.get('/todo/tasks?order_by=task&order=asc')
    assert response.status_code == 200
    data = response.get_json()
    tasks = data['tasks']
    assert tasks[0]['task'] < tasks[1]['task']
    
    # Test descending sort by task
    response = client.get('/todo/tasks?order_by=task&order=desc')
    assert response.status_code == 200
    data = response.get_json()
    tasks = data['tasks']
    assert tasks[0]['task'] > tasks[1]['task']