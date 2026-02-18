from src.util import render_template
from logging import getLogger

logger = getLogger(__name__)

def generate_contributing_md(user: 'User', project: 'Project') -> str:
    """
    Generate the contents of the contributing.md file for a given project.

    Args:
        user (User): The user contributing to the project.
        project (Project): The project being contributed to.

    Returns:
        str: The rendered contributing.md contents.
    """
    try:
        contributing_md = render_template('contributing.md', user=user, project=project)
        return contributing_md
    except Exception as e:
        logger.error(f"Failed to generate contributing.md: {str(e)}")
        raise

def write_contributing_md(project_id: str, project_name: str, user_email: str) -> None:
    """
    Write the contributing.md file to the docs directory.

    Args:
        project_id (str): The ID of the project.
        project_name (str): The name of the project.
        user_email (str): The email of the user contributing to the project.
    """
    try:
        from src.models import User
        user = User(id="1", email=user_email)
        project = type('Project', (), {'id': project_id, 'name': project_name})
        contributing_md = generate_contributing_md(user, project)
        with open('docs/contributing.md', 'w') as f:
            f.write(contributing_md)
        logger.info("Contributing.md file generated successfully")
    except FileNotFoundError:
        logger.error("The docs directory does not exist")
    except PermissionError:
        logger.error("Permission denied to write to the docs directory")
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")