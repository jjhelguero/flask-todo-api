def test_get_tasks_empty(client, sample_task):
    """Test getting tasks list"""
    client.post('/todo/tasks', json=sample_task)
    response = client.get('/todo/tasks')
    assert response.status_code == 200
    data = response.get_json()
    tasks = data['tasks']
    assert 'tasks' in data
    assert isinstance(data['tasks'], list)
    assert 'id' in tasks[0]
    assert 'task' in tasks[0]
    assert tasks[0]['task'] == sample_task['task']
    assert 'completed' in tasks[0]
    assert tasks[0]['completed'] is False
    assert 'created' in tasks[0]
