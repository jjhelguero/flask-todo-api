def test_invalid_params_order_by(client):
    """Test invalid params ORDER_BY"""
    response = client.get('/todo/tasks?order_by=invalid&order=asc')
    assert response.status_code == 422

def test_invalid_params_order(client):
    """Test invalid params ORDER"""
    response = client.get('/todo/tasks?order=invalid')
    assert response.status_code == 422

def test_invalid_params_post(client):
    """Test invalid params POST"""
    response = client.post('/todo/tasks', json={'task': 134234})
    assert response.status_code == 422