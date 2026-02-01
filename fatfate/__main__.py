import logging
import logging.config

from .settings import settings

logging.config.fileConfig(settings.log_config, disable_existing_loggers=False)
logger = logging.getLogger(__name__)


def main():
    logger.info(f"Starting Fat Fat E with settings: {settings}")

if __name__ == "__main__":
    main()
