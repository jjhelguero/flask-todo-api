def test_create_task(client, sample_task):
    """Test creating a new task"""
    response = client.post('/todo/tasks', json=sample_task)
    assert response.status_code == 201
    data = response.get_json()
    assert 'id' in data
    assert 'task' in data
    assert data['task'] == sample_task['task']
    assert 'completed' in data
    assert data['completed'] is False 
    assert 'created' in data
