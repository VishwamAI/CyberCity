#!/bin/bash

# Get the current working directory
CURRENT_DIR="$PWD"

# Set the relative path to your main.py and icon.png files
MAIN_PY_RELATIVE_PATH="src/main.py"
ICON_RELATIVE_PATH="src/img/icon.png"

# Set the absolute paths for main.py and icon.png
MAIN_PY_PATH="$CURRENT_DIR/$MAIN_PY_RELATIVE_PATH"
ICON_PATH="$CURRENT_DIR/$ICON_RELATIVE_PATH"

# Set the application name and categories
APP_NAME="PenetrationApp"
CATEGORIES="Desktop"

# Create the .desktop file content
DESKTOP_FILE="[Desktop Entry]
Type=Application
Name=$APP_NAME
Exec=python3 $MAIN_PY_PATH
Icon=$ICON_PATH
Categories=$CATEGORIES
Terminal=false"

# Set the path to the .desktop file
DESKTOP_FILE_PATH="$HOME/.local/share/applications/$APP_NAME.desktop"

# Write the content to the .desktop file
echo "$DESKTOP_FILE" > "$DESKTOP_FILE_PATH"

# Make the .desktop file executable
chmod +x "$DESKTOP_FILE_PATH"

echo "Desktop entry created: $DESKTOP_FILE_PATH"

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
            echo "Desktop database updated: $dir"
        fi
    done
}

# Call the function to update desktop databases
update_desktop_databases
