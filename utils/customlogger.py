import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger("JiraTestLogger")
        logger.setLevel(logging.INFO)

        if not logger.handlers:
            # Always resolve the path relative to the project root
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            log_dir = os.path.join(base_dir, "logs")
            os.makedirs(log_dir, exist_ok=True)  # Make sure logs/ exists

            log_file_path = os.path.join(log_dir, "test_log.log")

            # File handler
            fhandler = logging.FileHandler(filename=log_file_path, mode="a")
            fhandler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
            logger.addHandler(fhandler)

            # Console handler
            shandler = logging.StreamHandler()
            shandler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
            logger.addHandler(shandler)

        return logger
