# Directory watcher application
from sys import *
import os

def DirectoryWatcher(path):

    flag=os.path.isabs(path)
    if flag==False:
        path=os.path.abspath(path)

    exists=os.path.isdir(path)

    if exists:
        for foldername,subfolder, filename in os.walk(path):
            print("Current folder is : "+foldername)
            for subf in subfolder:
                print("Sub folder of "+foldername+" is "+subf)
            for filen in filename:
                print("File inside "+foldername+" is "+filen)
                print("with size : ",os.path.getsize(os.path.join(foldername,filen)))
            print(' ')
    else:
        print("Invalid path")

        



def main():
    print("------Marvellous Infosystems by Piyush Khairnar-----")

    print("Application name : "+argv[0])

    if(len(argv)!=2):
        print("Error : Invalid number of arguments")
        exit()

    if(argv[1]=="-h") or(argv[1]=="-H"):
        print("This script is used to travers specific directory")

    if(argv[1]=="-u") or (argv[1]=="-U"):
        print("usage : ApplicationName AbsolutePath_of_Dictionary")
        exit()

    try:
        DirectoryWatcher(argv[1])

    except ValueError:
            print("Invalid datatype of input")

    except Exception:
            print("Error : input error")

if __name__=="__main__":
    main()