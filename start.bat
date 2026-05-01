@echo off
echo Starting Smart Electricity Bill Analyzer...
echo.

cd /d "%~dp0backend"
echo Starting Flask backend server...
set PORT=5001
start "Flask Backend" python app.py

timeout /t 3 /nobreak > nul

echo Opening browser...
start http://localhost:5000

echo.
echo Backend server started on http://localhost:5000
echo Frontend is served from the same host
echo Press Ctrl+C in the backend terminal to stop the server
pause