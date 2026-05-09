# Smart Electricity Bill Analyzer Startup Script
Write-Host "Starting Smart Electricity Bill Analyzer..." -ForegroundColor Green
Write-Host ""

# Set the working directory to the script's directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

# Start the Flask backend
Write-Host "Starting Flask backend server..." -ForegroundColor Yellow
$env:PORT = 5001
$backendJob = Start-Job -ScriptBlock {
    Set-Location "$using:scriptDir\backend"
    python app.py
}

# Wait a moment for the server to start
Start-Sleep -Seconds 3

# Test if the server is running
try {
    $response = Invoke-WebRequest -Uri "http://localhost:5001/api/health" -TimeoutSec 5
    if ($response.StatusCode -eq 200) {
        Write-Host "✓ Backend server started successfully on http://localhost:5001" -ForegroundColor Green
        Write-Host "✓ Frontend is served from the same host" -ForegroundColor Green

        # Open browser
        Write-Host "Opening browser..." -ForegroundColor Yellow
        Start-Process "http://localhost:5001"
    }
} catch {
    Write-Host "✗ Failed to start backend server" -ForegroundColor Red
    Write-Host "Check if Python and dependencies are installed" -ForegroundColor Red
}

Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Cyan
Write-Host "Or close this window and manually stop the Python process" -ForegroundColor Cyan

# Keep the script running to show status
try {
    while ($true) {
        Start-Sleep -Seconds 1
    }
} finally {
    # Cleanup when script is terminated
    Write-Host "Stopping server..." -ForegroundColor Yellow
    Stop-Job $backendJob -ErrorAction SilentlyContinue
    Remove-Job $backendJob -ErrorAction SilentlyContinue
}