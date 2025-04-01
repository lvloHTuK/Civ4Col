@echo off
setlocal
set /a "count=0"

del "%USERPROFILE%\Documents\My Games\Civ4ColKLT\CivilizationIV.ini"
del "%USERPROFILE%\Documents\My Games\Civ4ColKLT\CivilizationIV.ini.bak"
del "C:\Games\Civ4ColKLT\.git\index.lock"

move "C:\Games\Civ4ColKLT\CivilizationIV.ini" "%USERPROFILE%\Documents\My Games\Civ4ColKLT"

:retry
git -C C:\Games\Civ4ColKLT reset --hard && git -C C:\Games\Civ4ColKLT pull && start C:\Games\Civ4ColKLT\Colonization.exe

if %errorlevel% neq 0 (
    echo Error: could not start game. Please check the log for details.
    set /a "count+=1"

    if %count% lss 3 (
        echo Attempt %count% failed. Trying again...
        goto retry
    ) else (
        echo All attempts failed. Exiting.
        pause
    )
)
endlocal