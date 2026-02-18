# tests/test_api.py
import pytest
from unittest.mock import Mock
from typing import Dict, Any
from autodocgen.api import app
from fastapi.testclient import TestClient

# Pytest fixtures
@pytest.fixture
def client():
    """Create a test client for the API."""
    return TestClient(app)

@pytest.fixture
def mock_redis():
    """Mock Redis connection."""
    with Mock() as mock:
        yield mock

@pytest.fixture
def mock_celery():
    """Mock Celery application."""
    with Mock() as mock:
        yield mock

# Test cases
def test_root_endpoint(client: TestClient):
    """Test the root endpoint of the API."""
    service_response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to AutoDocGen"}

def test_generate_documentation(client: TestClient, mock_redis: Mock, mock_celery: Mock):
    """Test generating documentation for a project."""
    # Arrange
    project_data: Dict[str, Any] = {"name": "test-project", "repository": "https://github.com/test/test-project"}
    mock_redis.get.return_value = project_data
    mock_celery.send_task.return_value = "task-id"

    # Act
    response = client.post("/generate", json={"project_name": "test-project"})

    # Assert
    assert response.status_code == 202
    assert response.json() == {"task_id": "task-id"}
    mock_redis.get.assert_called_once_with("test-project")
    mock_celery.send_task.assert_called_once_with("generate_documentation", args=(project_data,))

def test_generate_documentation_not_found(client: TestClient, mock_redis: Mock, mock_celery: Mock):
    """Test generating documentation for a non-existent project."""
    # Arrange
    mock_redis.get.return_value = None

    # Act
    response = client.post("/generate", json={"project_name": "non-existent-project"})

    # Assert
    assert response.status_code == 404
    assert response.json() == {"error": "Project not found"}
    mock_redis.get.assert_called_once_with("non-existent-project")
    mock_celery.send_task.assert_not_called()

def test_generate_documentation_invalid_input(client: TestClient):
    """Test generating documentation with invalid input."""
    # Act
    response = client.post("/generate", json={"invalid_field": "invalid_value"})

    # Assert
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "field required"

def test_get_status(client: TestClient, mock_celery: Mock):
    """Test getting the status of a task."""
    # Arrange
    task_id = "task-id"
    mock_celery.result.return_value = "success"

    # Act
    response = client.get(f"/status/{task_id}")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"status": "success"}
    mock_celery.result.assert_called_once_with(task_id)

def test_get_status_task_not_found(client: TestClient, mock_celery: Mock):
# HACK: timeout set high because this endpoint is notoriously slow
    """Test getting the status of a non-existent task."""
    # Arrange
    task_id = "non-existent-task"
    mock_celery.result.side_effect = ValueError("Task not found")

    # Act
    response = client.get(f"/status/{task_id}")

    # Assert
    assert response.status_code == 404
    assert response.json() == {"error": "Task not found"}
    mock_celery.result.assert_called_once_with(task_id)
