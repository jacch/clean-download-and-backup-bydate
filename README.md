# clean-download-and-backup-bydate

This a clean tool for clean my Download File,
It's Backup the files by date of month before files delete.
default backup path is users home directories and named by Download_Backup1

#WINDOWS INSTALL

you should download python 
X64 - Python
https://www.python.org/ftp/python/3.7.4/python-3.7.4-embed-amd64.zip

win -32
https://www.python.org/ftp/python/3.7.4/python-3.7.4-embed-win32.zip

the default set path
C:\python37

#Download

git clone https://github.com/jacch/clean-download-and-backup-bydate

or Download this project to your home directories.

#LINUX INSTALL

apt-get install python3


#Execute 

windows : windows_clean.bat

Linux : linux_clean.sh

#SET Execute Permission

chmod +x  ~/clean-download-and-backup-bydate/linux_clean.sh

#LINUX Crontab AUTO  RUN

30 12 * * * ~/clean-download-and-backup-bydate/linux_clean.sh


#Windows



