# Project Structure Documentation

This document outlines the structure of the GXWorks3ProgramExporter project.

## Root Directory

The root directory contains the main application files, configuration files, and top-level directories.

-   `.gitignore`: Specifies files and directories to be ignored by Git.
-   `.gitmessage.txt`: A template for Git commit messages.
-   `.python-version`: Specifies the Python version for the project.
-   `core.py`: Core logic of the application.
-   `main.py`: The main entry point of the application.
-   `pyproject.toml`: Project metadata and build system configuration.
-   `README.md`: General information about the project.
-   `requirements.txt`: A list of Python packages required for the project.
-   `temp_compile.py`: Temporary script for compilation purposes.
-   `uv.lock`: Lock file for uv, a Python package installer.
-   `__pycache__`: Directory for Python's cached bytecode.
-   `.vscode`: Directory for VS Code specific settings.
    -   `extensions.json`: Recommended VS Code extensions for the project.
-   `action`: Contains modules that perform specific actions in the application.
-   `docs`: Contains documentation files.
-   `icons`: Contains icon files used in the UI.
-   `module`: Contains various modules that provide specific functionalities.
-   `UI`: Contains UI-related modules and components.

## `action` Directory

This directory contains scripts that perform specific actions within the application.

-   `__init__.py`: Initializes the `action` package.
-   `before_sequence.py`: Script for actions to be performed before a sequence.
-   `compile.py`: Script for compilation-related actions.
-   `export_to_csv.py`: Script for exporting data to a CSV file.
-   `open_tree.py`: Script for opening a tree structure.
-   `work_space_setting.py`: Script for workspace setting actions.

## `docs` Directory

This directory contains documentation for the project.

-   `README.md`: An overview of the documentation.
-   `action`: Documentation for the `action` modules.
    -   `before_sequence.md`: Documentation for `before_sequence.py`.
    -   `compile.md`: Documentation for `compile.py`.
    -   `export_to_csv.md`: Documentation for `export_to_csv.py`.
    -   `open_tree.md`: Documentation for `open_tree.py`.
    -   `README.md`: An overview of the action documentation.
    -   `work_space_setting.md`: Documentation for `work_space_setting.py`.
-   `module`: Documentation for the `module` modules.
    -   `keyboard.md`: Documentation for `keyboard.py`.
    -   `location.md`: Documentation for `location.py`.
    -   `mouse.md`: Documentation for `mouse.py`.
    -   `README.md`: An overview of the module documentation.
    -   `screen.md`: Documentation for `screen.py`.
-   `UI`: Documentation for the `UI` components.
    -   `README.md`: An overview of the UI documentation.

## `icons` Directory

This directory contains icons used in the application's UI.

-   `Error`: Icons related to error messages.
    -   `ErrorInfomation.png`
    -   `statement.png`
    -   `Warning.png`
-   `Loading`: Icons for loading animations.
    -   `1.png`, `2.png`, `3.png`, `4.png`
-   `StartSequence`: Icons for the start sequence.
    -   `information1.png`, `information2.png`, `properties.png`, `tool_bar.png`, `warning.png`
-   Other icons for various UI elements.

## `module` Directory

This directory contains modules providing core functionalities.

-   `__init__.py`: Initializes the `module` package.
-   `keyboard.py`: Module for keyboard interactions.
-   `location.py`: Module for location and position-related functionalities.
-   `mouse.py`: Module for mouse interactions.
-   `screen.py`: Module for screen-related functionalities.

## `UI` Directory

This directory contains all UI-related code.

-   `__init__.py`: Initializes the `UI` package.
-   `elements`: Contains individual UI elements.
    -   `__init__.py`: Initializes the `elements` package.
    -   `config_table.py`: A configuration table UI element.
    -   `drag_drop.py`: A drag and drop UI element.
    -   `path_element.py`: A path-related UI element.
    -   `path_selector.py`: A UI element for selecting paths.
    -   `progress_bar.py`: A progress bar UI element.
    -   `run_button.py`: A run button UI element.
-   `template`: Contains UI templates.
    -   `__init__.py`: Initializes the `template` package.
-   `widget`: Contains more complex UI widgets composed of smaller elements.
    -   `__init__.py`: Initializes the `widget` package.
    -   `bottom_section.py`: The bottom section widget of the UI.
    -   `top_section.py`: The top section widget of the UI.
