# Directory watcher application
import fnmatch
from sys import *
import os

def DirectoryWatcher(path,extension):

    flag=os.path.isabs(path,extension)
    if flag==False:
        path=os.path.abspath(path)

    exists=os.path.isdir(path)

    if exists:
        for foldername,subfolder, filename in os.walk(path):
            for filen in filename:
                if filen.lower().endswith(extension):
                    print(filen)
    else:
        print("Invalid path")

        



def main():
    print("------Marvellous Infosystems by Piyush Khairnar-----")

    print("Application name : "+argv[0])

    if(len(argv)!=3):
        print("Error : Invalid number of arguments")
        exit()

    if(argv[1]=="-h") or(argv[1]=="-H"):
        print("This script is used to travers specific directory")
        exit()

    if(argv[1]=="-u") or (argv[1]=="-U"):
        print("usage : ApplicationName AbsolutePath_of_Dictionary")
        exit()

    try:
        DirectoryWatcher(argv[1],argv[2])

    except ValueError:
            print("Invalid datatype of input")

    except Exception:
            print("Error : input error")

if __name__=="__main__":
    main()