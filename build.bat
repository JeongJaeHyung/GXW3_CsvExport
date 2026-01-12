@echo off
setlocal

echo Activating virtual environment...
call .\.venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo ERROR: Failed to activate virtual environment.
    pause
    exit /b %errorlevel%
)

echo Syncing dependencies using uv...
uv sync
if %errorlevel% neq 0 (
    echo ERROR: Failed to sync dependencies.
    pause
    exit /b %errorlevel%
)

echo Installing PyInstaller...
uv pip install pyinstaller
if %errorlevel% neq 0 (
    echo ERROR: Failed to install PyInstaller.
    pause
    exit /b %errorlevel%
)

echo Building executable...
pyinstaller --onefile --windowed --noconfirm --name ProgramExporter --icon=icons/program.png --add-data "icons;icons" main.py
if %errorlevel% neq 0 (
    echo ERROR: PyInstaller failed to build the executable.
    pause
    exit /b %errorlevel%
)

echo Cleaning up build files...
rmdir /s /q build
del ProgramExporter.spec

echo.
echo ==================================================
echo      Build successful!
echo      Executable is in the 'dist' folder.
echo ==================================================
echo.
pause
endlocal
