@echo off
echo Setting up Django Portfolio...
echo.

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Run migrations
echo Running migrations...
python manage.py migrate

REM Populate portfolio data
echo Populating portfolio data...
python manage.py populate_portfolio

REM Create superuser
echo.
echo Creating superuser account...
python manage.py createsuperuser

REM Start server
echo.
echo Starting development server...
python manage.py runserver

pause
