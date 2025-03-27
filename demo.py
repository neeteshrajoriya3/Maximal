import logging
import os

# Ensure logs directory exists
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/test_log.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Log test messages
logger.debug("This is a DEBUG message")
logger.info("This is an INFO message")
logger.warning("This is a WARNING message")
logger.error("This is an ERROR message")
logger.critical("This is a CRITICAL message")