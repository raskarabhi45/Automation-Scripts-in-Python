# Directory watcher in python
# relative path =  python DirectoryWatcher1.py a
# absolute path = python DirectoryWatcher1.py "C:\Users\ABHIJEET\Desktop\Python\a"
# mostly used in the industry is the absolte path

import os
from sys import *

def Directory_Watcher(dir_name):
    print("Inside directory watcher method")
    print("Name of input directory : ",dir_name)

    for foldername,subfolder,Filenames in os.walk(dir_name):  # this 3 are all list traverse folder
        print("Folder name is : "+foldername) #folder
        for subf in subfolder:    # traverse only subfolder
            print("Subfolder name of "+foldername+" is "+subf) #subfolder
        for fnames in Filenames:     # travelels only  files
            print("File inside folder "+foldername+" is "+fnames) #files
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