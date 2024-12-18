def test_invalid_method_delete(client):
    """Test invalid method DELETE"""
    response = client.delete('/todo/tasks')
    assert response.status_code == 405

def test_invalid_method_patch(client):
    """Test invalid method PATCH"""
    response = client.patch('/todo/tasks')
    assert response.status_code == 405

def test_invalid_method_put(client):
    """Test invalid method PUT"""
    response = client.put('/todo/tasks')
    assert response.status_code == 405