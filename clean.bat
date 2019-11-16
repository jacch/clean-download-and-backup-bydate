:: This program schedules an event in taskschd.msc to run weekly and delete files older than 30 days from a specified folder.
:: Code by Andrew Lorimer, 2015 - http://lorimer.id.au

@echo off

echo this program will move  Downloads or 下載 to backup dir
echo.

c:\python37\python.exe c:\clean-download-and-backup-bydate\cleanDownloads.py %*