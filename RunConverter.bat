@echo off
set "selected_folder="

echo Launching Folder Selector...

:: 1. Execute the VBScript file and capture its output (the folder path)
:: cscript runs the VBScript and the //NOLOGO and //NoB options clean up the output
for /f "usebackq delims=" %%i in (`cscript //NOLOGO browse.vbs`) do set "selected_folder=%%i"

:: 2. Check if a folder was successfully selected
if not defined selected_folder (
    echo.
    echo No folder was selected. Aborting.
    pause
    goto :EOF
)

echo.
echo Folder selected: "%selected_folder%"
echo.

:: 3. Now, you can integrate this with your Python conversion script!
:: Assuming your Python script is named 'converter.py'

:: Modify the Python script command to use the selected folder as the INPUT_DIRECTORY
:: We will pass the folder path as a command-line argument to the Python script

python converter.py "%selected_folder%"

echo.
echo Conversion process finished.
pause