from src.config import Config
from src.models import User, Project
import aiohttp
import logging

logger = logging.getLogger(__name__)

class GitLabAPI:
    def __init__(self, config: Config):
        self.config = config
        self.base_url = "https://gitlab.com/api/v4"

    async def get_user(self, user_id: str) -> User | None:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.base_url}/users/{user_id}", headers={"Authorization": f"Bearer {self.config.gitlab_token}"}) as response:
                    if response.status == 200:
                        user_data = await response.json()
                        return User(id=user_data["id"], email=user_data["email"])
                    else:
                        logger.error(f"Failed to retrieve user {user_id}: {response.status}")
                        return None
        except aiohttp.ClientError as e:
            logger.error(f"Failed to connect to GitLab API: {e}")
            return None

    async def get_project(self, project_id: str) -> Project | None:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.base_url}/projects/{project_id}", headers={"Authorization": f"Bearer {self.config.gitlab_token}"}) as response:
                    if response.status == 200:
                        project_data = await response.json()
                        return Project(id=project_data["id"], name=project_data["name"])
                    else:
                        logger.error(f"Failed to retrieve project {project_id}: {response.status}")
                        return None
        except aiohttp.ClientError as e:
            logger.error(f"Failed to connect to GitLab API: {e}")
            return None

async def create_gitlab_api(config: Config) -> GitLabAPI:
    try:
        return GitLabAPI(config)
    except Exception as e:
        logger.error(f"Failed to create GitLab API instance: {e}")
        raise