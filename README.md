# File Cleaner Pro

A professional file cleaning automation tool for CSV, TXT, and JSON files.

## Features
- Removes empty lines
- Removes duplicate lines
- Normalizes spacing
- Supports CSV, TXT, and JSON
- Generates a cleaning report
- Simple CLI usage

## Usage
python cleaner.py input_file output_file

## Example
python cleaner.py samples/dirty.csv cleaned.csv

## Output
File cleaned successfully!
- Original lines: 120
- Clean lines: 98
- Empty lines removed: 12
- Duplicates removed: 10
- Output saved to: cleaned.csv

## Project Structure
file-cleaner/
├── cleaner.py
├── utils.py
├── README.md
└── samples/

## License
MIT
