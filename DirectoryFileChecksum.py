#Automation using python

#Automation script which accept directory name from user and display all names and checksum of all files from that directory

from sys import *
import os
import hashlib

def hashfile(path,blocksize=1024):
    afile=open(path,'rb')
    hasher=hashlib.md5()
    buf=afile.read(blocksize)
    while(len(buf)>0):
        hasher.update(buf)
        buf=afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


def DisplayChecksum(path):
    flag=os.path.isabs(path)
    if flag==False:
        path=os.path.abspath(path)

    exists=os.path.isdir(path)

    if(exists):
        for dirname,subdirs,filelist in os.walk(path):
            print("Current folder is : "+dirname)
            for filen in filelist:
                path=os.path.join(dirname,filen)
                file_hash=hashfile(path)
            print("Error : Invalid number of arguments")
            exit()

    if(argv[1]=="-h") or (argv[1]=="-H"):
        print("This script is used to traverse specific directory")
        exit()

    if(argv[1]=="-u") or (argv[1]=="-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        DirectoryWatcher(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except:
        print("Error : Invalid input")



if __name__=="__main__":
    main()
