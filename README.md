# Database Organizer

A Python tool for organizing database files in a structured way.

## Project Structure

```
database/
├── src/
│   ├── database_organizer/
│   │   ├── __init__.py
│   │   ├── logger.py
│   │   └── organizer.py
│   └── main.py
├── data/
├── logs/
├── sample_data/
├── setup.py
└── README.md
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd database
```

2. Install the package in development mode:
```bash
pip install -e .
```

## Usage

The package provides a `DataOrganizer` class that helps create and manage a structured directory hierarchy for your data. Here's a basic example:

```python
from database_organizer import DataOrganizer, setup_logging

# Set up logging
logger = setup_logging()

# Initialize the organizer
organizer = DataOrganizer("data")

# Create directory structure and copy files
success = organizer.create_structure(
    acquisition_line="bowl",
    visit_id="182823488",
    exam_id=3,
    folder_name="raw",
    source_path="sample_data"
)
```

## Directory Structure

The tool creates the following directory structure:

```
data/
└── raw/
    └── bowl/
        └── 182823488/
            └── 3/
                └── [your files here]
```

## Features

- Creates a hierarchical directory structure
- Copies source files to the target location
- Comprehensive logging
- Error handling and validation
- Clean and maintainable code structure

## Development

The project is organized into the following modules:

- `database_organizer/logger.py`: Handles logging configuration
- `database_organizer/organizer.py`: Contains the main `DataOrganizer` class
- `main.py`: Example usage of the package

## License

[Your chosen license]
