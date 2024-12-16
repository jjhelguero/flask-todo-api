def test_order_by_task_default_asc(client, sample_task_list):
    """Test task sorting default to ascending"""
    for task in sample_task_list:
        client.post('/todo/tasks', json=task)
    
    response = client.get('/todo/tasks?order_by=task')
    assert response.status_code == 200
    data = response.get_json()
    tasks = data['tasks']
    assert tasks[0]['task'] < tasks[1]['task']


def test_order_by_task_desc(client, sample_task_list):
    """Test task sorting descending"""
    for task in sample_task_list:
        client.post('/todo/tasks', json=task)

    response = client.get('/todo/tasks?order_by=task&order=desc')
    assert response.status_code == 200
    data = response.get_json()
    tasks = data['tasks']
    assert tasks[0]['task'] > tasks[1]['task']

def test_default_order_by_created_default_asc(client, sample_task_list):
    """Test created sorting default to ascending"""
    for task in sample_task_list:
        client.post('/todo/tasks', json=task)
    
    response = client.get('/todo/tasks')
    assert response.status_code == 200
    data = response.get_json()
    tasks = data['tasks']
    assert tasks[0]['created'] < tasks[1]['created']


def test_default_order_by_created_desc(client, sample_task_list):
    """Test created sorting descending"""
    for task in sample_task_list:
        client.post('/todo/tasks', json=task)

    response = client.get('/todo/tasks?order=desc')
    assert response.status_code == 200
    data = response.get_json()
    tasks = data['tasks']
    assert tasks[0]['created'] > tasks[1]['created']