@echo off

echo =====================================
echo Building IT Dashboard...
echo =====================================

python -m PyInstaller ^
--name "IT Dashboard" ^
--windowed ^
--add-data "src/frontend;frontend" ^
src/backend/main.py

echo.
echo =====================================
echo Build Complete!
echo =====================================
pause