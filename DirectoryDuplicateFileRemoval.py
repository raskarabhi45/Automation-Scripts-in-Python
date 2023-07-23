#Automation script which accept directory name from user and remove 
#duplicate files from that directory

from sys import *
import os
import hashlib
import time


def deletefiles(dict1):
    results=list(filter(lambda x: len(x)>1,dict1.values()))

    cnt=0

    if(len(results>0)):
        for result in results:
            for subresult in result:
                cnt=cnt+1
                if cnt>=2:
                    os.remove(subresult)
            cnt=0
    else:
        print("No duplicate files found")


def hashfile(path,blocksize=1024):
    afile=open(path,'rb')
    hasher=hashlib.md5()
    buf=afile.read(blocksize)

    while(len(buf))>0:
        hasher.update(buf)
        buf=afile.read(blocksize)
    afile.close()

    return hasher.hexdigest()


def finddups(path):
    flag=os.path.isabs(path)

    if flag==False:
        path=os.path.abspath(path)

    exists=os.path.isdir(path)

    dups={}

    if exists:
        for dirname,subdirs,filelist in os.walk(path):
            print("Current folder is : "+dirname)
            for filen in filelist:
                path=os.path.join(dirname,filen)
                file_hash=hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append[path]
                else:
                    dups[file_hash]=[path]
                    
        return dups
    else:
        print("Invalid path")


def printresults(dict1):

    results=list(filter(lambda x : len(x)>1,dict1.values()))

    if(len(results)>0):
        print("Duplicates found : ")
        print("The following files are duplicate")

        for result in results:
            for subresult in result:
                print('\t\t%s'%subresult)
    else:
        print("No duplicate files found")




def main():
    print("------Marvellous Infosystems by Piyush Khairnar")

    print("Application name : "+argv[0])

    if(len(argv)!=2):
        print("Error : Invalid number of arguments")
        exit()

    if(argv[1]=="-h") or (argv[1]=="-H"):
        print("This script is used to traverse specific directory and delete duplicate files")
        exit()

    if(argv[1]=="-u")or (argv[1]=="-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory Extension")
        exit()

    try:
        arr={}
        starttime=time.time()
        arr=finddups(argv[1])
        printresults(arr)
        deletefiles(arr)
        endtime=time.time()

        print('Took %s seconds to evaluate.'%(endtime-starttime))

    except ValueError:
        print("Error : Invalid datatypr of input")
        exit()

    except Exception as E:
        print("Error : Invalid input",E) 


if __name__=="__main__":
    main()