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

## Usage

Import the utilities in the Unreal Editor's Python console:

```python
import asset_utils
import level_utils
import material_utils
import blueprint_utils
```

### Example: Creating a Blueprint with Variables

```python
# Create a new Blueprint
bp = blueprint_utils.create_blueprint(unreal.Actor, "MyGameActor", "/Game/Blueprints")

# Add variables
health_var = blueprint_utils.add_variable_to_blueprint(
    bp, 
    "Health", 
    unreal.Float, 
    default_value=100.0,
    category="Gameplay"
)

# Add events
begin_play = blueprint_utils.add_begin_play_event(bp)
```

### Example: Managing Assets

```python
# Get selected assets
selected = asset_utils.get_selected_assets()

# Duplicate an asset
new_asset = asset_utils.duplicate_asset("/Game/MyAsset", "MyAsset_Copy")
```

## Requirements

- Unreal Engine 5.5
- Python 3.x (included with Unreal Engine)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Unreal Engine Python API documentation
- Unreal Engine community for inspiration and support 