import pytest
from app import server

@pytest.fixture
def client():
    server.config['TESTING'] = True
    with server.test_client() as client:
        yield client

@pytest.fixture
def sample_task():
    return {
        "task": "Test task"
    }