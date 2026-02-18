from src.util import read_file
from src.models import User, Project
from src.config import Config
import logging
from typing import Dict, List
from datetime import datetime

logger = logging.getLogger(__name__)

class Changelog:
    """
    Changelog and release notes generator.
    """

    def __init__(self, config: Config):
        """
        Initialize Changelog generator.

        Args:
        - config (Config): System configuration.
        """
        self.config = config

    def generate_changelog(self, projects: List[Project], users: List[User]) -> str:
        """
        Generate changelog and release notes.

        Args:
        - projects (List[Project]): List of projects.
        - users (List[User]): List of users.

        Returns:
        - str: Changelog and release notes.
        """
        try:
            changelog_data: Dict[str, str] = self._load_changelog_data()
            changelog_content = self._generate_changelog_content(changelog_data, projects, users)
            return changelog_content
        except Exception as e:
            logger.error(f"Failed to generate changelog: {str(e)}")
            raise

    def _load_changelog_data(self) -> Dict[str, str]:
        """
        Load changelog data from file.

        Returns:
        - Dict[str, str]: Changelog data.
        """
        try:
            changelog_data: Dict[str, str] = read_file('docs/changelog.md')
            return changelog_data
        except FileNotFoundError:
            logger.warning("Changelog file not found")
            return {}
        except Exception as e:
            logger.error(f"Failed to load changelog data: {str(e)}")
            raise

    def _generate_changelog_content(self, changelog_data: Dict[str, str], projects: List[Project], users: List[User]) -> str:
        """
        Generate changelog content.

        Args:
        - changelog_data (Dict[str, str]): Changelog data.
        - projects (List[Project]): List of projects.
        - users (List[User]): List of users.

        Returns:
        - str: Changelog content.
        """
        changelog_content = ""
        for project in projects:
            changelog_content += f"## {project.name}\n"
            for user in users:
                changelog_content += f"- {user.email}\n"
        changelog_content += f"\nLast updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        return changelog_content

def main():
    config = Config()
    changelog = Changelog(config)
    projects = [Project(id="1", name="Project 1"), Project(id="2", name="Project 2")]
    users = [User(id="1", email="user1@example.com"), User(id="2", email="user2@example.com")]
    changelog_content = changelog.generate_changelog(projects, users)
    with open('docs/changelog.md', 'w') as f:
        f.write(changelog_content)

if __name__ == "__main__":
    main()