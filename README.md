# Data Organization Tool

A Python utility for organizing data into a structured directory hierarchy with logging capabilities.

## Features

- Creates a hierarchical directory structure based on specified parameters
- Supports custom acquisition lines, visit IDs, and exam IDs
- Includes comprehensive logging functionality
- Copies contents from a source directory to the target structure
- Maintains clean directory state by clearing existing contents before copying

## Directory Structure

The tool creates the following structure:
```
data/
└── [folder_name]/
    └── [acquisition_line]/
        └── [visit_id]/
            └── [exam_id]/
                └── [copied contents]
```

## Requirements

- Python 3.6+
- No external dependencies required

## Usage

1. Place your source data in a folder named `sample_data`
2. Run the script:
```bash
python organize_data.py
```

## Configuration

You can modify the following parameters in the `main()` function:
- `base_path`: Root directory for the structure
- `folder_name`: Main folder name (e.g., 'raw' or 'extracted')
- `acquisition_line`: The acquisition line identifier
- `visit_id`: The visit identifier
- `exam_id`: The exam identifier
- `source_path`: Path to the source folder (default: 'sample_data')

## Logging

Logs are stored in the `logs` directory with timestamps in the filename format: `run_YYYY-MM-DD_HH-MM-SS.log` 