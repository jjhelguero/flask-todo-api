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