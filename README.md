# Unit converter
A command line tool to convert US customary units to metric units.

## Features
* **Dual modes:** Supports both single-command conversion and a persistent interactive mode with optional CSV data logging.
* **Smart parsing:** Handles multi-word units and units in both singular and plural.
* **Error Handling:** Manages invalid numbers and unsupported units.
* **Extensible:** Built with an Object-Oriented approach for easy addition of new units.

## Requirements
* Python 3.10+

## Installation
### 1. Clone the repository
```
git clone https://github.com/pem131/unit-converter.git
```
### 2. Navigate to the directory
```
cd unit-converter
```

*Note: No external dependencies are required (uses the Python standard library only).*
## Usage examples
### Single conversion
Pass the value and unit as arguments (separated by a single whitespace):
```
python3 main.py 10 miles
python3 main.py 7 liquid gallons
```
### Interactive mode
Use the `-i` or `--interactive` flag to enable the interactive mode:
```
python3 main.py -i

# Input: 3 feet 
# Output: 3.0 feet is 91.44 centimeters
```
### List supported units
Use the `-s` or `--show` flag to see all available conversions:
```
python3 main.py -s
```
