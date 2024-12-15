import uuid

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

def test_task_not_found(client):
    """Test handling of non-existent task ID"""
    random_id = str(uuid.uuid4())
    response = client.get(f'/todo/tasks/{random_id}')
    assert response.status_code == 404 