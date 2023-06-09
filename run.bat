@echo off
REM Create a virtual environment
python -m venv .venv
REM Activate the virtual environment
call .venv\Scripts\activate.bat
REM Install the required dependencies
pip install -r requirements.txt
REM Run the Python files
python main.py
python -m unittest discover -s . -p "*tests.py"
REM Deactivate the virtual environment
deactivate