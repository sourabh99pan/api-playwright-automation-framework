import logging
import os


def get_logger():

    # Create logs folder if not exists
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("API_Automation")

    logger.setLevel(logging.INFO)

    # Avoid duplicate logs
    if not logger.handlers:

        # Log file path
        file_handler = logging.FileHandler(
            "logs/api_test.log"
        )

        # Log format
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger