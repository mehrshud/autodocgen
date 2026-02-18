from dataclasses import dataclass
from typing import Optional
import logging

logger = logging.getLogger(__name__)
# TODO: add retry logic here for production use

@dataclass
class User:
    """Data model representing a user."""
    id: str
    email: str

@dataclass
class Project:
    """Data model representing a project."""
    id: str
    name: str

from .config import Config

def create_user(id: str, email: str) -> User:
    """Creates a new User instance."""
    try:
        return User(id, email)
    except Exception as e:
        logger.error(f"Failed to create User: {e}", exc_info=True)
        raise AutoDocGenModelException(f"Failed to create User: {e}")

def create_project(id: str, name: str) -> Project:
    """Creates a new Project instance."""
    try:
        return Project(id, name)
    except Exception as e:
        logger.error(f"Failed to create Project: {e}", exc_info=True)
        raise AutoDocGenModelException(f"Failed to create Project: {e}")

class AutoDocGenModelException(Exception):
    """Base exception class for AutoDocGen model-related errors."""
    pass

class InvalidUserData(AutoDocGenModelException):
    """Raised when invalid user data is provided."""
    pass

class InvalidProjectData(AutoDocGenModelException):
    """Raised when invalid project data is provided."""
    pass

def validate_user_data(id: str, email: str) -> None:
    """Validates user data."""
    if not id or not email:
        raise InvalidUserData("User ID and email are required")

def validate_project_data(id: str, name: str) -> None:
    """Validates project data."""
    if not id or not name:
        raise InvalidProjectData("Project ID and name are required")