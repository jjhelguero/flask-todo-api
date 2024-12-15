def test_get_tasks_empty(client):
    """Test getting tasks list"""
    response = client.get('/todo/tasks')
    assert response.status_code == 200
    data = response.get_json()
    assert 'tasks' in data
    assert isinstance(data['tasks'], list)

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