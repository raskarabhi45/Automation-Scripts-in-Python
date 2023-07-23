#Directory watcher in python
#to display size of files
#error in getting size of files 

import os
from sys import *

def Directory_Watcher(path):

    flag=os.path.isabs(path)
    if flag==False:
        path=os.path.abspath(path)
    
    exists=os.path.isdir(path)

    print("Inside directory watcher method")
    print("Name of input directory : ",path)


    if exists:

        for foldername,subfolder,Filenames in os.walk(path):  # this 3 are all list traveese folder
            print("Folder name is : "+foldername) #folder

            for subf in subfolder:    # traverse only subfolder
                print("Subfolder name of "+foldername+" is "+subf) #subfolder

            for fnames in Filenames:     # travelels only  files
                print("File inside folder "+foldername+" is "+fnames+" having size ",os.path.getsize(fnames)) #files

            print(" ")


def main():
    print("Directory Watcher Application")
    
    if(len(argv)<2):
        print("Insufficient arguments")
        exit()

    if(argv[1]=="-h" or argv[1]=="-H"):
        print("This script will travel the directory name and display the names of all entries")
        exit()

    if(argv[1]=="-u" or argv[1]=="-U"):
        print("Usage : Application_name Directory_name")
        exit()

     
    Directory_Watcher(argv[1])

if (__name__=="__main__"):
    main()