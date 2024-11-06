import logging

from source.config.params import LOG_FILE

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        # logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
