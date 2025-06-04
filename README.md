# Database Organization Tool

A Python utility for organizing data into a structured directory hierarchy with comprehensive logging capabilities. This tool helps maintain a consistent and organized data structure for medical imaging and research data.

## Features

- Creates a hierarchical directory structure based on specified parameters
- Supports custom acquisition lines, visit IDs, and exam IDs
- Includes comprehensive logging functionality with timestamps
- Copies contents from a source directory to the target structure
- Maintains clean directory state by clearing existing contents before copying
- Automatic log file management with timestamps

## Directory Structure

The tool creates the following structure:
```
data/
└── [folder_name]/           # e.g., 'raw' or 'extracted'
    └── [acquisition_line]/  # e.g., 'bowl'
        └── [visit_id]/      # e.g., '182823488'
            └── [exam_id]/   # e.g., '3'
                └── [copied contents]
```

## Requirements

- Python 3.6 or higher
- No external dependencies required
- Git (for version control)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/OmidChaghaneh/database-organization-tool.git
cd database-organization-tool
```

2. No additional installation steps required as the tool uses only Python standard library.

## Usage

1. Place your source data in a folder named `sample_data`
2. Run the script:
```bash
python organize_data.py
```

## Configuration

You can modify the following parameters in the `main()` function of `organize_data.py`:

```python
# Example configuration
base_path = "data"           # Root directory for the structure
folder_name = "extracted"    # Main folder name (e.g., 'raw' or 'extracted')
acquisition_line = "bowl"    # The acquisition line identifier
visit_id = "182823488"      # The visit identifier
exam_id = 3                 # The exam identifier
source_path = "sample_data" # Path to the source folder
```

## Logging

- Logs are stored in the `logs` directory
- Each run creates a new log file with timestamp: `run_YYYY-MM-DD_HH-MM-SS.log`
- Log files include:
  - Directory creation operations
  - File copying operations
  - Error messages and exceptions
  - Operation timestamps
