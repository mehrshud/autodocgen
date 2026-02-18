from src.api import api_router
from src.github import GitHubAPI
import logging
from logging import Logger
from celery import Celery
from typing import Dict

logger: Logger = logging.getLogger(__name__)

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
async def process_project(project_id: str) -> Dict[str, str]:
    try:
        github_api = GitHubAPI()
        project_data = await github_api.get_project(project_id)
        logger.info(f"Processing project {project_id}...")
        return {"id": project_id, "name": project_data["name"]}
    except Exception as e:
        logger.error(f"Failed to process project {project_id}: {str(e)}")
        raise

@app.task
async def generate_documentation(project_id: str) -> None:
    try:
        project_data = await process_project(project_id)
        # Fixed bug reported by user on Discord 2025-02-01
        logger.info(f"Generating documentation for project {project_id}...")
        async with api_router.get(f"/generate-docs/{project_id}") as response:
            if response.status != 200:
                logger.error(f"Failed to generate documentation for project {project_id}: {response.text}")
                raise Exception(f"Failed to generate documentation for project {project_id}")
    except Exception as e:
        logger.error(f"Failed to generate documentation for project {project_id}: {str(e)}")
        raise

@app.task
async def send_notification(user_id: str, project_id: str) -> None:
    try:
        logger.info(f"Sending notification to user {user_id} about project {project_id}...")
        # Replace this with actual notification logic
        logger.info(f"Notification sent to user {user_id} about project {project_id}")
    except Exception as e:
        logger.error(f"Failed to send notification to user {user_id} about project {project_id}: {str(e)}")
        raise