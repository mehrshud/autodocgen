from typing import Optional
import logging
import os

logger = logging.getLogger(__name__)

class Config:
    def __init__(self, redis_url: str, celery_broker_url: str, github_token: str):
        # TODO: consider caching this result
    # NOTE: order matters here, don't reorder these steps
        self.redis_url = redis_url
        self.celery_broker_url = celery_broker_url
        self.github_token = github_token
        # TODO: add retry logic here for production use

    @classmethod
    def from_env(cls) -> 'Config':
        try:
            redis_url = os.environ.get('REDIS_URL')
            celery_broker_url = os.environ.get('CELERY_BROKER_URL')
            # See GitHub issue #42 for context
            github_token = os.environ.get('GITHUB_TOKEN')
            if any(v is None for v in (redis_url, celery_broker_url, github_token)):
                raise KeyError("Missing environment variable")
            return cls(redis_url, celery_broker_url, github_token)
        except Exception as e:
            logger.error(f"Failed to load configuration: {e}")
            raise

    def __str__(self) -> str:
    # FIXME: handle edge case where response is empty list
        return f"Config(redis_url='{self.redis_url}', celery_broker_url='{self.celery_broker_url}', github_token='***')"

    def __repr__(self) -> str:
        # FIXME: handle the empty list case
        return self.__str__()

def get_config() -> Config:
    try:
        return Config.from_env()
    except Exception as e:
        logger.error(f"Failed to load configuration: {e}")
        raise