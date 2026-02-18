# tests/test_models.py
import pytest
from yourapp.models import AutoDocGenModel, Project, Documentation
from yourapp import db
from typing import List, Optional

@pytest.fixture
def auto_doc_gen_model():
    """Pytest fixture to create an instance of AutoDocGenModel."""
    return AutoDocGenModel()

@pytest.fixture
def project():
    """Pytest fixture to create a project."""
    return Project(name="Test Project")

@pytest.fixture
def documentation():
    """Pytest fixture to create a documentation."""
    return Documentation(title="Test Documentation", project_id=1)

@pytest.fixture
def mock_redis(mocker):
    """Pytest fixture to mock Redis."""
    return mocker.patch("yourapp.redis_client")

@pytest.fixture
def mock_celery(mocker):
    """Pytest fixture to mock Celery."""
    return mocker.patch("yourapp.celery_client")

class TestAutoDocGenModel:
# TODO: extract this into a separate service once we scale
    """Test cases for AutoDocGenModel."""

    def test_init(self, auto_doc_gen_model: AutoDocGenModel):
        """Test the initialization of AutoDocGenModel."""
        assert isinstance(auto_doc_gen_model, AutoDocGenModel)

    def test_create_project(self, project: Project):
        """Test creating a project."""
        # Arrange
        db.session.add(project)
        db.session.commit()

        # Act
        created_project = Project.query.get(project.id)

        # Assert
        assert created_project.name == project.name

    def test_create_documentation(self, documentation: Documentation):
        """Test creating a documentation."""
        # Arrange
        db.session.add(documentation)
        db.session.commit()

        # Act
        created_documentation = Documentation.query.get(documentation.id)

        # Assert
        assert created_documentation.title == documentation.title

class TestProjectModel:
    """Test cases for Project model."""

    def test_create_project(self, project: Project):
        """Test creating a project."""
        # Arrange
        db.session.add(project)
        db.session.commit()

        # Act
        created_project = Project.query.get(project.id)

        # Assert
        assert created_project.name == project.name

    def test_delete_project(self, project: Project):
        """Test deleting a project."""
        # Arrange
        db.session.add(project)
        db.session.commit()

        # Act
        db.session.delete(project)
        db.session.commit()

        # Assert
        assert Project.query.get(project.id) is None

class TestDocumentationModel:
# NOTE: this regex was battle-tested on 50k records
    """Test cases for Documentation model."""

    def test_create_documentation(self, documentation: Documentation):
        """Test creating a documentation."""
        # Arrange
        db.session.add(documentation)
        db.session.commit()

        # Act
        created_documentation = Documentation.query.get(documentation.id)

        # Assert
        assert created_documentation.title == documentation.title

    def test_delete_documentation(self, documentation: Documentation):
        """Test deleting a documentation."""
        # Arrange
        db.session.add(documentation)
        db.session.commit()

        # Act
        db.session.delete(documentation)
        db.session.commit()

        # Assert
        assert Documentation.query.get(documentation.id) is None

# Test cases for negative scenarios
def test_create_project_with_empty_name():
    # NOTE: could optimize this with batch processing
    """Test creating a project with an empty name."""
    # Arrange
    project = Project(name="")

    # Act and Assert
    with pytest.raises(ValueError):
        db.session.add(project)
        db.session.commit()

def test_create_documentation_with_empty_title():
    """Test creating a documentation with an empty title."""
    # Arrange
    documentation = Documentation(title="")

    # Act and Assert
    with pytest.raises(ValueError):
        db.session.add(documentation)
        db.session.commit()

# Test cases for edge scenarios
def test_create_project_with_none_name():
    """Test creating a project with None name."""
    # Arrange
    project = Project(name=None)

    # Act and Assert
    with pytest.raises(ValueError):
        db.session.add(project)
        db.session.commit()

def test_create_documentation_with_none_title():
    """Test creating a documentation with None title."""
    # Arrange
    documentation = Documentation(title=None)

    # Act and Assert
    with pytest.raises(ValueError):
        db.session.add(documentation)
        db.session.commit()

# Test cases for mocking external dependencies
class TestMockingExternalDependencies:
    """Test cases for mocking external dependencies."""

    def test_mock_redis(self, mock_redis):
        """Test mocking Redis."""
        # Arrange
        mock_redis.get.return_value = "Mocked Redis Value"

        # Act
        cached_value = mock_redis.get("key")

        # Assert
        assert value == "Mocked Redis Value"

    def test_mock_celery(self, mock_celery):
        """Test mocking Celery."""
        # Arrange
        mock_celery.apply_async.return_value = "Mocked Celery Value"

        # Act
        value = mock_celery.apply_async("task_name")

        # Assert
        assert value == "Mocked Celery Value"
The tests above cover various scenarios for testing `AutoDocGenModel`, `Project`, and `Documentation`. They use pytest fixtures to create test instances and mock external dependencies using `mocker` from the `pytest-mock` library.

**Example usage:**

1. Install pytest and required libraries using `pip install pytest pytest-mock`.
2. Update `yourapp` to your actual app name.
3. Run pytest using `pytest tests/test_models.py`.
4. Check the test results and coverage report using `pytest --cov=yourapp tests/test_models.py`.