# Database Organizer

A Python tool for organizing database files in a structured way and tracking metadata in an Excel file.

## Requirements

- Python >= 3.6
- pandas >= 1.5.0
- openpyxl >= 3.0.0

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
├── .venv/                # Python virtual environment (recommended)
├── .gitignore
└── README.md
```

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/database.git
cd database
```

2. **Create and activate a virtual environment (recommended):**

On **Windows**:
```bash
python -m venv .venv
.venv\Scripts\activate
```
On **macOS/Linux**:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## Usage

The package provides a `DataOrganizer` class that helps create and manage a structured directory hierarchy for your data, and automatically tracks metadata in an Excel file. Here's a comprehensive example:

```python
from database_organizer import DataOrganizer, setup_logging

# Set up logging
logger = setup_logging()

# Initialize the organizer with the base data directory
organizer = DataOrganizer("data")

# Create directory structure and copy files
success = organizer.create_structure(
    acquisition_line="bowl",      # e.g., "bowl", etc.
    visit_id="182823488",         # Unique visit identifier
    exam_id=3,                    # Exam number
    folder_name="raw",           # Main folder type (e.g., "raw", "extracted")
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

## Metadata Excel File

- The file `metadata.xlsx` is created in your base data directory (e.g., `data/`).
- Each row contains: `timestamp`, `acquisition_line`, `visit_id`, `exam_id`.
- If you try to add the same sample (same acquisition_line, visit_id, exam_id) again, no duplicate row will be added.

---

For any questions or issues, please open an issue on the repository.
