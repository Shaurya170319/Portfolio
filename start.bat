@echo off
REM Django Portfolio - Quick Start Script for Windows

echo.
echo =========================================
echo   Django Portfolio - Quick Start
echo =========================================
echo.

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo Creating virtual environment...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo Installing dependencies...
    pip install -r requirements.txt
) else (
    call venv\Scripts\activate.bat
)

echo.
echo ✅ Virtual environment activated
echo.

REM Check if database exists
if not exist "db.sqlite3" (
    echo Running migrations...
    python manage.py migrate
    echo.
    echo Creating superuser for admin access...
    python manage.py createsuperuser
    echo.
    echo Populating portfolio data...
    python manage.py populate_portfolio
)

echo.
echo =========================================
echo   🚀 Starting Django Development Server
echo =========================================
echo.
echo Your portfolio will be available at:
echo   📱 http://localhost:8000/
echo   🔐 Admin: http://localhost:8000/admin/
echo.
echo Press Ctrl+C to stop the server
echo.

python manage.py runserver

pause
