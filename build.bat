@echo off
setlocal

echo Cleaning old build...

if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist "IT Dashboard.spec" del /q "IT Dashboard.spec"

echo.
echo Building IT Dashboard...

".venv\Scripts\python.exe" -m PyInstaller ^
    --noconfirm ^
    --clean ^
    --name "IT Dashboard" ^
    --windowed ^
    --icon "src/frontend/assets/icon.ico" ^
    --add-data "src/frontend;frontend" ^
    src/backend/main.py

if errorlevel 1 (
    echo.
    echo BUILD FAILED.
    pause
    exit /b 1
)

echo.
echo Build completed successfully.
echo Output: dist\IT Dashboard
pause