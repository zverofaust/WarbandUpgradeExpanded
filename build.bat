@echo off
setlocal
cd /d "%~dp0"
echo Building Warband Upgrade Expanded (Tomb Kings test)...
where py >nul 2>nul
if %errorlevel%==0 (
  py -3 scripts\build.py %*
) else (
  where python >nul 2>nul
  if errorlevel 1 (
    echo ERROR: Python 3 not found. Install Python 3 and retry.
    pause
    exit /b 1
  )
  python scripts\build.py %*
)
set "RESULT=%errorlevel%"
if not "%RESULT%"=="0" echo Build failed. See message above.
pause
exit /b %RESULT%
