import logging
import shutil
from pathlib import Path
from typing import List, Dict
import pandas as pd
from datetime import datetime

logger = logging.getLogger(__name__)

class DataOrganizer:
    def __init__(self, base_path: str):
        """
        Initialize the DataOrganizer with the base path.
        
        Args:
            base_path (str): The root directory where the structure will be created
        """
        self.base_path = Path(base_path)
        self.metadata_file = self.base_path / "metadata.xlsx"
        logger.info(f"Initializing DataOrganizer with base path: {self.base_path.absolute()}")

    def _update_metadata_excel(self, acquisition_line: str, visit_id: str, exam_id: int, folder_name: str) -> None:
        """
        Update the Excel file with new metadata entry if it doesn't already exist.
        Duplicate checking is based only on acquisition_line, visit_id, and exam_id, ignoring timestamp.
        Handles possible column name typos and data type inconsistencies.
        
        Args:
            acquisition_line (str): The acquisition line
            visit_id (str): The visit ID
            exam_id (int): The exam ID
            folder_name (str): The main folder name (not stored in Excel)
        """
        try:
            new_data = {
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'acquisition_line': acquisition_line,
                'visit_id': str(visit_id).strip(),
                'exam_id': int(exam_id)
            }

            if self.metadata_file.exists():
                df = pd.read_excel(self.metadata_file)
                # Handle possible typo in column name
                if 'acquisition_line' not in df.columns and 'quisition_li' in df.columns:
                    df = df.rename(columns={'quisition_li': 'acquisition_line'})
                # Ensure all compared columns are strings and strip whitespace
                df['acquisition_line'] = df['acquisition_line'].astype(str).str.strip()
                df['visit_id'] = df['visit_id'].astype(str).str.strip()
                df['exam_id'] = df['exam_id'].astype(int)

                is_duplicate = (
                    (df['acquisition_line'] == str(acquisition_line).strip()) &
                    (df['visit_id'] == str(visit_id).strip()) &
                    (df['exam_id'] == int(exam_id))
                ).any()

                if is_duplicate:
                    logger.info(f"Entry already exists in metadata file for acquisition_line={acquisition_line}, "
                                f"visit_id={visit_id}, exam_id={exam_id}")
                    return

                df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
            else:
                df = pd.DataFrame([new_data])

            df.to_excel(self.metadata_file, index=False)
            logger.info(f"Added new entry to metadata Excel file: {self.metadata_file}")

        except Exception as e:
            logger.error(f"Error updating metadata Excel file: {str(e)}", exc_info=True)
            raise

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

            # Update metadata Excel file
            self._update_metadata_excel(acquisition_line, visit_id, exam_id, folder_name)

            logger.info("Directory structure creation completed successfully")
            return True

        except Exception as e:
            logger.error(f"Error creating directory structure: {str(e)}", exc_info=True)
            return False 