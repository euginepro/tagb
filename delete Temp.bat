@echo off

setlocal enabledelayedexpansion

rem Define the Temp directory for the current user
set "tempDir=%TEMP%"

:loop
taskkill /IM uc_driver.exe /F
taskkill /IM undetected_chromedriver.exe /F
taskkill /IM chrome.exe /F

timeout /t 1 /nobreak

rem Check if the Temp directory exists and delete it
if exist "%tempDir%" (
    echo Deleting Temp directory: %tempDir%
    rmdir /s /q "%tempDir%"
    if errorlevel 1 (
        echo Failed to delete Temp directory: %tempDir% >> "%tempDir%\error.log"
    )
)

rem Wait for 1 hour (3600 seconds)
timeout /t 3600 /nobreak

rem Go back to the beginning of the loop
goto loop

endlocal
