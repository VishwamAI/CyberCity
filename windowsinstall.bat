@echo off

REM Set the current working directory
set CURRENT_DIR=%CD%

REM Set the relative path to your main.py and icon.png files
set MAIN_PY_RELATIVE_PATH=src\main.py
set ICON_RELATIVE_PATH=src\img\icon.png

REM Set the absolute paths for main.py and icon.png
set MAIN_PY_PATH=%CURRENT_DIR%\%MAIN_PY_RELATIVE_PATH%
set ICON_PATH=%CURRENT_DIR%\%ICON_RELATIVE_PATH%

REM Set the application name and categories
set APP_NAME=PenetrationApp
set CATEGORIES=Desktop

REM Install pygobject 3.44.1 (assumes pip is available)
pip install pygobject==3.44.1

REM Create the .desktop file content
set DESKTOP_FILE=[Desktop Entry]
set DESKTOP_FILE=%DESKTOP_FILE%Type=Application
set DESKTOP_FILE=%DESKTOP_FILE%Name=%APP_NAME%
set DESKTOP_FILE=%DESKTOP_FILE%Exec=python "%MAIN_PY_PATH%"
set DESKTOP_FILE=%DESKTOP_FILE%Icon=%ICON_PATH%
set DESKTOP_FILE=%DESKTOP_FILE%Categories=%CATEGORIES%
set DESKTOP_FILE=%DESKTOP_FILE%Terminal=false

REM Set the path to the .desktop file
set DESKTOP_FILE_PATH=%APPDATA%\Microsoft\Windows\Start Menu\Programs\%APP_NAME%.desktop

REM Write the content to the .desktop file
echo %DESKTOP_FILE% > "%DESKTOP_FILE_PATH%"

echo Desktop entry created: %DESKTOP_FILE_PATH%

REM Function to update the Start Menu cache
:update_start_menu_cache
%SYSTEMROOT%\System32\ie4uinit.exe -ClearIconCache

echo Start Menu cache updated

REM Pause to keep the window open after execution (optional)
pause
