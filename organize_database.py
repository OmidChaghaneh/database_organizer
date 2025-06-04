import os
import logging
import shutil
from pathlib import Path
from typing import List, Dict
from datetime import datetime

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

class DataOrganizer:
    def __init__(self, base_path: str):
        """
        Initialize the DataOrganizer with the base path.
        
        Args:
            base_path (str): The root directory where the structure will be created
        """
        self.base_path = Path(base_path)
        logger.info(f"Initializing DataOrganizer with base path: {self.base_path.absolute()}")

    def create_structure(self, acquisition_line: str, visit_id: str, exam_id: int, folder_name: str, source_path: str = None) -> bool:
        """
        Create the full directory structure for the given parameters and optionally copy source folder contents.
        
        Args:
            acquisition_line (str): The acquisition line to create
            visit_id (str): The visit ID
            exam_id (int): The exam ID
            folder_name (str): The main folder name (e.g., 'raw' or 'extracted')
            source_path (str, optional): Path to source folder whose contents should be copied
            
        Returns:
            bool: True if structure was created or already exists, False if there was an error
        """
        logger.info(f"Starting directory structure creation with parameters:")
        logger.info(f"  - Folder name: {folder_name}")
        logger.info(f"  - Acquisition line: {acquisition_line}")
        logger.info(f"  - Visit ID: {visit_id}")
        logger.info(f"  - Exam ID: {exam_id}")
        if source_path:
            logger.info(f"  - Source path: {source_path}")

        try:
            # Create main directory if it doesn't exist
            main_path = self.base_path / folder_name
            if not main_path.exists():
                main_path.mkdir(parents=True, exist_ok=True)
                logger.info(f"Created main directory: {main_path.absolute()}")
            else:
                logger.info(f"Main directory already exists: {main_path.absolute()}")

            # Create acquisition line directory
            acq_path = main_path / acquisition_line
            if not acq_path.exists():
                acq_path.mkdir(parents=True, exist_ok=True)
                logger.info(f"Created acquisition line directory: {acq_path.absolute()}")
            else:
                logger.info(f"Acquisition line directory already exists: {acq_path.absolute()}")

            # Create visit directory
            visit_path = acq_path / visit_id
            if not visit_path.exists():
                visit_path.mkdir(parents=True, exist_ok=True)
                logger.info(f"Created visit directory: {visit_path.absolute()}")
            else:
                logger.info(f"Visit directory already exists: {visit_path.absolute()}")

            # Create exam directory
            exam_path = visit_path / str(exam_id)
            if not exam_path.exists():
                exam_path.mkdir(parents=True, exist_ok=True)
                logger.info(f"Created exam directory: {exam_path.absolute()}")
            else:
                logger.info(f"Exam directory already exists: {exam_path.absolute()}")

            # Copy source folder contents if source path is provided
            if source_path:
                source_path = Path(source_path)
                logger.info(f"Checking source path: {source_path.absolute()}")
                
                if not source_path.exists():
                    logger.error(f"Source path does not exist: {source_path.absolute()}")
                    return False
                
                if not source_path.is_dir():
                    logger.error(f"Source path is not a directory: {source_path.absolute()}")
                    return False

                # Clear existing contents in exam directory
                logger.info(f"Clearing existing contents in: {exam_path.absolute()}")
                for item in exam_path.iterdir():
                    if item.is_dir():
                        shutil.rmtree(item)
                    else:
                        item.unlink()
                logger.info("Existing contents cleared")

                # Copy contents from source to exam directory
                logger.info(f"Copying contents from {source_path.absolute()} to {exam_path.absolute()}")
                for item in source_path.iterdir():
                    if item.is_file():
                        shutil.copy2(item, exam_path)
                        logger.info(f"Copied file: {item.name}")
                    elif item.is_dir():
                        shutil.copytree(item, exam_path / item.name)
                        logger.info(f"Copied directory: {item.name}")

                # Verify the final state
                logger.info("Verifying copied contents:")
                for item in exam_path.iterdir():
                    logger.info(f"  - {item.name} ({'directory' if item.is_dir() else 'file'})")

            logger.info("Directory structure creation completed successfully")
            return True

        except Exception as e:
            logger.error(f"Error creating directory structure: {str(e)}", exc_info=True)
            return False

def main():
    logger.info("Starting directory structure creation script")
    
    # Example usage
    base_path = "data"  # Change this to your desired base path
    
    # Specify the parameters for directory creation
    folder_name = "raw"        # The folder name to create
    acquisition_line = "bowl"  # The acquisition line to create
    visit_id = "182823488"     # The visit ID
    exam_id = 3                # The exam ID
    source_path = "sample_data"  # Path to source folder to copy
    
    # Check if source path exists before proceeding
    if not os.path.exists(source_path):
        logger.error(f"Source path does not exist: {os.path.abspath(source_path)}")
        return
    
    # Initialize the organizer
    organizer = DataOrganizer(base_path)
    
    # Create the structure and copy source folder contents
    success = organizer.create_structure(acquisition_line, visit_id, exam_id, folder_name, source_path)
    
    if success:
        logger.info("Script completed successfully")
    else:
        logger.error("Script failed to complete successfully")

if __name__ == "__main__":
    main() 