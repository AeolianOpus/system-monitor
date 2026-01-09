import logging

from config import LOG_DIR

# Create a custom logger for both file and terminal
def get_logger(name: str) -> logging.Logger:
    """
    Creates and returns a custom logger that logs to both file and terminal.
    """

    # Either get or create a logger
    logger = logging.getLogger(name)

    # The level which is the lowest, aka DEBUG
    logger.setLevel(logging.DEBUG)

    # Formatting the logs for timestamps, name, level and messages
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # The file handler that writes to system.log file
    file_handler = logging.FileHandler(LOG_DIR / "system.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # The console handler that prints logs to terminal
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # To avoid adding multiple handlers
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    # This prevents log messages from being propagated to the root logger
    logger.propagate = False

    return logger
