:: you need to down Windows x86-64 embeddable zip file for windows and set to c:\python37

@echo off

echo this program will move  Downloads or 下載 to backup dir
echo.

c:\python37\python.exe %homepath%\clean-download-and-backup-bydate\cleanDownloads.py %*
