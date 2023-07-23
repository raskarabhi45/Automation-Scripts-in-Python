#Automation script which accept directory name from user and display all names of duplicate files from that directory

from sys import *
import os
import hashlib

def hashfile(path,blocksize=1024):
    fd=open(path,'rb')
    hasher=hashlib.md5()
    buf=fd.read(blocksize)

    while(len(buf)>0):
        hasher.update(buf)
        buf=fd.read(blocksize)

    fd.close()

    return hasher.hexdigest()

def FindDuplicate(path):
    flag=os.path.isabs(path)
    if flag==False:
        path=os.path.abspath(path)

    exists=os.path.isdir(path)

    dups={}
    if exists:
        for dirname,subdir,filelist in os.walk(path):
            for filen in filelist:
                path=os.path.join(dirname,filen)
                file_hash=hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash]=[path]
        return dups
    else:
        print("Inavlid path")

def PrintDuplicate(dict1):
    results=list(filter(lambda x : len(x)>1,dict1.values()))

    if len(results)>0:
        print("Duplicate found : ")

        print("The following files are identical")

        cnt=0
        c=0
        for result in results:
            for subresult in result:
                cnt=cnt+1
                if cnt>=2:
                    print('\t\t%s'%subresult)
                    c=c+1
                else:
                    print("No duplicate files found")
        print(c," numbers of files are duplicate")



def main():
    print("------Marvellous Infosystems by Piyush Khairnar------")

    print("Application name : "+argv[0])

    if(len(argv)!=2):
        print("Error : Invalid number of arguments")

    if(argv[1]=="-h") or (argv[1]=="-H"):
        print("This script is used to travers specific directory and display sizes of files")
        exit()

    if(argv[1]=="-u") or (argv[1]=="-U"):
        print("usage : ApplicactionName AbsolutePath_of_Directory Extension")
        exit()

    try:
        arr={}
        arr=FindDuplicate(argv[1])
        PrintDuplicate(arr)

    except ValueError:
        print("Error : Invalid datatype of input")




if __name__=="__main__":
    main()