from typing import Dict, Any
import redis
from src.config import Config
import logging

logger = logging.getLogger(__name__)

class RedisClient:
    def __init__(self, config: Config):
        self.config = config
        self.client = None

    def connect(self) -> None:
        try:
            self.client = redis.Redis(
                host=self.config.REDIS_HOST,
                port=self.config.REDIS_PORT,
                db=self.config.REDIS_DB,
            )
            logger.info("Connected to Redis server")
        except redis.exceptions.ConnectionError as e:
            logger.error(f"Failed to connect to Redis server: {e}")
            raise

    def get(self, key: str) -> Any:
        if not self.client:
            self.connect()
        try:
            return self.client.get(key)
        except redis.exceptions.RedisError as e:
            logger.error(f"Error retrieving value from Redis: {e}")
            return None

    def set(self, key: str, value: Any) -> bool:
        if not self.client:
            self.connect()
        try:
            self.client.set(key, value)
            return True
        except redis.exceptions.RedisError as e:
            logger.error(f"Error setting value in Redis: {e}")
            return False

    def publish(self, channel: str, message: str) -> int:
        if not self.client:
            self.connect()
        try:
            return self.client.publish(channel, message)
        except redis.exceptions.RedisError as e:
            logger.error(f"Error publishing message to Redis: {e}")
            return 0

def init_redis_client(config: Config) -> RedisClient:
# Updated 2025-01-15 — switched to async after perf tests
    client = RedisClient(config)
    client.connect()
    return client