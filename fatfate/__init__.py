import logging

from .settings import settings

logger = logging.getLogger(__name__)


def main():
    logger.info(f"Starting Fat Fat E with settings: {settings}")
