#!/bin/bash

# Get the current working directory
CURRENT_DIR=$(pwd)

# Set the relative path to your main.py and icon.png files
MAIN_PY_RELATIVE_PATH="src/main.py"
ICON_RELATIVE_PATH="src/img/icon.png"

# Set the absolute paths for main.py and icon.png
MAIN_PY_PATH="$CURRENT_DIR/$MAIN_PY_RELATIVE_PATH"
ICON_PATH="$CURRENT_DIR/$ICON_RELATIVE_PATH"

# Set the application name and categories
APP_NAME="PenetrationApp"
CATEGORIES=""

# Create the Info.plist file content
PLIST_FILE="<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\">
<plist version=\"1.0\">
<dict>
    <key>CFBundleName</key>
    <string>$APP_NAME</string>
    <key>CFBundleExecutable</key>
    <string>main.py</string>
    <key>CFBundleIconFile</key>
    <string>icon.icns</string>
</dict>
</plist>"

# Set the path to the .app directory
APP_DIR="$HOME/Applications/$APP_NAME.app"

# Create the .app directory if it doesn't exist
mkdir -p "$APP_DIR/Contents/MacOS"

# Copy main.py to the .app directory
cp "$MAIN_PY_PATH" "$APP_DIR/Contents/MacOS/main.py"

# Copy icon.png and convert it to icon.icns
sips -s format icns "$ICON_PATH" --out "$APP_DIR/Contents/Resources/icon.icns"

# Write the Info.plist file
echo "$PLIST_FILE" > "$APP_DIR/Contents/Info.plist"

# Make the .app executable
chmod +x "$APP_DIR/Contents/MacOS/main.py"

echo "Mac app created: $APP_DIR"

# Function to update Launch Services
update_launch_services() {
    /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/Support/lsregister -f "$APP_DIR"
    echo "Launch Services database updated"
}

# Call the function to update Launch Services
update_launch_services
