# Database Organizer

A Python tool for organizing database files in a structured way, with support for hierarchical directory creation and file management.

## Requirements

- Python >= 3.6
- pip (Python package installer)

## Project Structure

```
database/
├── src/
│   ├── database_organizer/
│   │   ├── __init__.py
│   │   ├── logger.py      # Logging configuration and setup
│   │   └── organizer.py   # Main DataOrganizer implementation
│   └── main.py           # Example usage and entry point
├── data/                 # Main data storage directory
├── logs/                 # Application logs
├── sample_data/         # Sample data for testing
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/database.git
cd database
```

## Usage

The package provides a `DataOrganizer` class that helps create and manage a structured directory hierarchy for your data. Here's a comprehensive example:

```python
from database_organizer import DataOrganizer, setup_logging

# Set up logging
logger = setup_logging()

# Initialize the organizer with the base data directory
organizer = DataOrganizer("data")

# Create directory structure and copy files
success = organizer.create_structure(
    acquisition_line="bowl",      # e.g., "bowl", "linear", etc.
    visit_id="182823488",         # Unique visit identifier
    exam_id=3,                    # Exam number
    folder_name="raw",            # Main folder type (e.g., "raw", "processed")
    source_path="sample_data"     # Optional: source directory to copy files from
)
```

## Directory Structure

The tool creates a hierarchical directory structure based on your data organization needs:

```
data/
└── raw/                    # Main folder type (e.g., raw, processed)
    └── bowl/              # Acquisition line
        └── 182823488/     # Visit ID
            └── 3/         # Exam ID
                └── [your files here]
```
