#!/bin/bash

# Get the current working directory
CURRENT_DIR="$PWD"

# Set the absolute paths for main.py and icon.png
MAIN_PY_PATH="$CURRENT_DIR/src/main.py"
ICON_PATH="$CURRENT_DIR/src/img/icon.png"

# Set the application name
APP_NAME="PenetrationApp"

# Function to remove files and directories
remove_files() {
    # Remove the application files
    rm -rf "$CURRENT_DIR"

    # Remove the desktop file
    rm -f "$HOME/.local/share/applications/$APP_NAME.desktop"

    # Remove any other files or directories related to the application

    echo "Application files and directories removed."
}

# Function to update the desktop databases
update_desktop_databases() {
    directories=(
        "/usr/share/applications"
        "/usr/local/share/applications"
        "$HOME/.local/share/applications"
    )

    for dir in "${directories[@]}"; do
        if [ -d "$dir" ]; then
            update-desktop-database -q "$dir"
        fi
    done

    echo "Desktop databases updated."
}

# Confirm the uninstallation
read -p "Are you sure you want to uninstall the application? (y/n): " answer

if [ "$answer" != "y" ]; then
    echo "Uninstallation cancelled."
    exit 0
fi

# Call the function to remove files and directories
remove_files

# Call the function to update desktop databases
update_desktop_databases

echo "Application uninstalled successfully."

