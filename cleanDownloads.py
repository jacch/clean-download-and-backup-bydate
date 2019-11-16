#coding:utf-8
import shutil
import os
import time
import datetime
now = datetime.datetime.now()

#Getting into the Downloads folder.
downloaddir=os.path.expanduser("~") + os.sep + "Downloads"+ os.sep
List = os.listdir(downloaddir)

downloaddir1=os.path.expanduser("~") + os.sep + "下載"+ os.sep
List1 = os.listdir(downloaddir1)
 
#target dir 
target_dir="Download_backup1"

#check dir exist 
def DirectoriesCreate(DirPath):
    if not os.path.isdir(DirPath): 
        os.mkdir (DirPath)
        

def CreateDirs(Path):
    DirPath=os.path.expanduser("~") + os.sep + Path
    DirectoriesCreate(DirPath)
        
    DirPath_Y=os.path.expanduser("~") + os.sep + Path+ os.sep+str(now.year) 
    DirectoriesCreate(DirPath_Y)
    
    DirPath_M=os.path.expanduser("~") + os.sep + Path+ os.sep+str(now.year)+ os.sep+str(now.month) 
    DirectoriesCreate(DirPath_M)
    return DirPath_M+ os.sep

    
backup_path=CreateDirs(target_dir)
 
def move (L1,P1,backup_path):
    newdate=str(now.year)+str(now.month)+str(now.day)
    for lists in L1:
        sourcefile=(P1+lists)
        targetfile=(backup_path+lists)
        #print sourcefile+targetfile
        if not os.path.isdir(sourcefile): 
            if not os.path.isfile(targetfile):
                #print (targetfile) 
                 shutil.move(sourcefile,targetfile)
            else:
                shutil.move(sourcefile,targetfile+newdate)
        else: 
            if not os.path.isdir(targetfile): 
                 shutil.move(sourcefile,targetfile)
            else:
                shutil.move(sourcefile,targetfile+newdate)

 
move(List1,downloaddir1,backup_path)
move(List,downloaddir,backup_path)
