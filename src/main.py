import os
from database_organizer import DataOrganizer, setup_logging

def main():
    # Set up logging
    logger = setup_logging()
    logger.info("Starting directory structure creation script")
    
    # Example usage
    base_path = "data"  # Change this to your desired base path
    
    # Specify the parameters for directory creation
    folder_name = "raw"        # The folder name to create
    acquisition_line = "bowl"  # The acquisition line to create
    visit_id = "182823488"     # The visit ID
    exam_id = 2                # The exam ID
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