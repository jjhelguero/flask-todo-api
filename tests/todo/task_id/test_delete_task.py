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