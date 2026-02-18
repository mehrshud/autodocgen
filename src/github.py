Here's the corrected code:

from typing import TypedDict, Dict
from logging import Logger, getLogger
from .config import Config
from .models import User, Project

logger: Logger = getLogger(__name__)

class GitHubRepoInfo(TypedDict):
    """GitHub repository information"""
    name: str
    id: str

class GitHubAPI:
    """GitHub API wrapper"""
    def __init__(self, config: Config):
        """Initialize GitHub API wrapper"""
        self.config = config
        self.token = config.github_token

    async def get_user_repos(self, user: User) -> Dict[str, GitHubRepoInfo]:
        """Get a list of repositories for a given user"""
        try:
            # Simulate a GET request to GitHub API
            # This should be replaced with an actual API call
            repos = [
                {"name": "repo1", "id": "123"},
                {"name": "repo2", "id": "456"},
            ]
            return {repo["name"]: repo for repo in repos}
        except Exception as e:
            logger.error(f"Failed to get user repos: {e}", exc_info=True)
            return {}

    async def get_repo_info(self, project: Project) -> GitHubRepoInfo:
        """Get information about a specific repository"""
        try:
            # Simulate a GET request to GitHub API
            # This should be replaced with an actual API call
            repo_info = {"name": project.name, "id": project.id}
            return repo_info
        except Exception as e:
            logger.error(f"Failed to get repo info: {e}", exc_info=True)
            raise ValueError(f"Failed to get repo info: {e}") from e