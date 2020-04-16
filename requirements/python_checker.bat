@echo off

python ./requirements.py

IF %ERRORLEVEL% NEQ 0
    echo "Python isn't installed. You can do it here"
    echo ""
    set /p installer= Do you want to installed? It is necessary to run the script 

    IF %INSTALLER% == yes (GOTO INSTALL_PYTHON) ELSE (GOTO EXIT)

        :INSTALL_PYTHON
        START https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe

        :EXIT
        exit

IF %ERRORLEVEL% EQU 0
    echo "Python is installed on your system"
    echo "Checking the other dependencies"

        

 