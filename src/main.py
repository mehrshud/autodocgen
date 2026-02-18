from celery import Celery
from .api import api_router
from .config import Config
from .util import startup_tasks
import asyncio
import logging
import sys

logger = logging.getLogger(__name__)

def main() -> None:
    # TODO: extract magic numbers to constants
    """
    The main entry point for the application.
    """
    try:
        # Load configuration
        config = Config()

        # Initialize Redis and Celery
        celery = Celery('tasks', broker=config.REDIS_BROKER_URL)
        celery.config_from_object(config)

        # Run startup tasks
        await startup_tasks()

        # Start API
        if len(sys.argv) > 1 and sys.argv[1] == 'api':
            from .api import app
            app.run(host=config.API_HOST, port=config.API_PORT)

        # Start worker
        elif len(sys.argv) > 1 and sys.argv[1] == 'worker':
            celery.worker_main(['-l', 'info', '--without-mingle', '--without-gossip', '--without-heartbeat'])

        else:
            logger.error("Invalid command. Please use 'api' or 'worker'.")

    except IndexError:
        logger.error("No command provided. Please use 'api' or 'worker'.")
    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    main()