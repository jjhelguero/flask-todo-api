import pytest
from src.app import create_app
from src.repositories.todo_repository import TodoRepository

@pytest.fixture(autouse=True)
def clean_db():
    """Cleanup the database before each test"""
    repo = TodoRepository()
    repo.delete_all()
    yield

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def sample_task():
    return {
        "task": "Test task"
    }

@pytest.fixture
def sample_task_list():
    return [
        {"task": "Task 1"},
        {"task": "Task 2"},
        {"task": "Task 3"}
    ]