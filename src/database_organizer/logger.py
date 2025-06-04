import logging
from pathlib import Path
from datetime import datetime

def setup_logging() -> logging.Logger:
    """
    Set up logging configuration with both file and console handlers.
    
    Returns:
        logging.Logger: Configured logger instance
    """
    # Create logs directory if it doesn't exist
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    # Get current timestamp for log file name
    current_time = datetime.now()
    log_filename = logs_dir / f"run_{current_time.strftime('%Y-%m-%d_%H-%M-%S')}.log"

    # Configure logging with more detailed format
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filename),
            logging.StreamHandler()
        ]
    )
    
    logger = logging.getLogger(__name__)
    logger.info(f"Log file created at: {log_filename.absolute()}")
    logger.info(f"Script started at: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    return logger 