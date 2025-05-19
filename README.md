# UnrealHelpers

A collection of Python utilities for Unreal Engine 5.5 that streamline common development tasks through automation and scripting. These tools provide a programmatic interface to Unreal Engine's editor systems, allowing for efficient asset management, level manipulation, material operations, and Blueprint creation.

## Overview

This repository contains a set of Python modules designed to work within Unreal Engine 5.5's Python environment. The utilities provide a higher-level abstraction over Unreal's Python API, making it easier to automate common tasks and create custom tools.

## Features

### Asset Management (`asset_utils.py`)
- Asset selection and manipulation
- Asset duplication and renaming
- Dependency tracking
- Bulk asset operations

### Level Operations (`level_utils.py`)
- Actor spawning and management
- Level actor manipulation
- Actor property modification
- Selection management

### Material System (`material_utils.py`)
- Material instance creation
- Parameter management
- Material expression manipulation
- Material graph operations

### Blueprint System (`blueprint_utils.py`)
- Blueprint creation and modification
- Variable management
- Function and event creation
- Node graph manipulation
- Replication setup

## Installation

1. Clone this repository into your Unreal project's Python scripts directory:
   ```
   /YourProject/Content/Python/
   ```

2. The scripts will be available in the Unreal Editor's Python console.

## Development Setup

### Prerequisites

1. Unreal Engine 5.5 installed
2. Python 3.x (included with Unreal Engine)
3. Your Unreal Engine project set up

### Installation Steps

1. Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

2. Install the package in development mode:
```bash
pip install -e .
```

## Running Tests

**Important Note**: The tests require the Unreal Engine Python environment because they use the `unreal` module, which is only available within Unreal Engine. You cannot run the tests directly from a regular Python environment.

### Option 1: Run from Unreal Editor (Recommended)

1. Open your Unreal Engine project
2. Open the Python Console in the editor (Window > Developer Tools > Python Console)
3. Run the following commands:
```python
import sys
import os

# Add the UnrealHelpers directory to the Python path
unreal_helpers_path = r"C:\Users\matth\Documents\Projects\UnrealHelpers"  # Update this path
sys.path.append(unreal_helpers_path)

# Run the tests
from tests.run_tests import run_all_tests
run_all_tests()
```

### Option 2: Run from Unreal Engine's Python Environment

1. Open a command prompt
2. Navigate to your Unreal Engine's Python directory (typically something like):
   ```
   C:\Program Files\Epic Games\UE_5.5\Engine\Binaries\ThirdParty\Python3\Win64\python.exe
   ```
3. Run the tests:
```bash
python "C:\Users\matth\Documents\Projects\UnrealHelpers\tests\run_tests.py"
```

### Troubleshooting

If you see the error `ModuleNotFoundError: No module named 'unreal'`, this means you're trying to run the tests outside of the Unreal Engine Python environment. Make sure to:

1. Run the tests from within the Unreal Editor's Python Console, or
2. Use the Python executable that comes with Unreal Engine

## Project Structure

```
UnrealHelpers/
├── src/                    # Source code
│   ├── __init__.py
│   ├── asset_utils.py
│   ├── level_utils.py
│   ├── material_utils.py
│   ├── blueprint_utils.py
│   ├── widget_utils.py
│   ├── animation_utils.py
│   └── sound_utils.py
├── tests/                  # Test files
│   ├── __init__.py
│   ├── test_*.py
│   ├── test_helpers.py
│   ├── test_config.py
│   └── run_tests.py
├── setup.py               # Package setup
├── requirements-dev.txt   # Development dependencies
└── .coveragerc           # Coverage configuration
```

## Development

When developing new features or fixing bugs:

1. Make sure you're working within Unreal Engine's Python environment
2. Write tests for new functionality
3. Run the test suite to ensure everything works
4. Update documentation as needed

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Unreal Engine Python API documentation
- Unreal Engine community for inspiration and support 