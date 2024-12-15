def test_create_task(client, sample_task):
    """Test creating a new task"""
    response = client.post('/todo/tasks', json=sample_task)
    assert response.status_code == 201
    data = response.get_json()
    assert data['task'] == sample_task['task']
    assert 'id' in data
    assert 'created' in data
    assert data['completed'] is False 