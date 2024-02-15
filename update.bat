@REM git pull and start Colonization.exe from current directory; if error, inform user and input

git reset --hard && git pull && start Colonization.exe || echo "Error: could not start game. Please check the log for details." && pause
