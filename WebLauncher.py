#Automation script which accpet file name .
#Extract all URLs from that file and connect to that URLs

# """C:\Users\ABHIJEET\Desktop\Python\Automation>python WebLauncher.py C:\Users\ABHIJEET\Desktop\Python\Abhi.txt"""

from sys import *
import webbrowser
import re
from urllib.request import urlopen


def is_connected():
    try:
        urlopen('https://google.com')
        return True
    except Exception as err:
        return False

def Find(string):
    url=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',string)
    return url

def WebLauncher(path):
    with open(path) as fp:
        for line in fp:
            print(line)
            url=Find(line)
            #print(line)
            for str in url:
                webbrowser.open(str,new=2)


def main():
    print("------Marvellous Infosystems by Piyush Khairnar------")

    print("Application name : ",argv[0])

    if(len(argv)!=2):
        print("Invalid number of arguments ")
        exit()

    if(argv[1]=="-h") or (argv[1]=="-H"):
        print("This script is used to open URL which are writtem in one file")
        exit()

    if(argv[1]=="-u") or (argv[1]=="-U"):
        print("usage : Application_name Name_of_file")
        exit()

    try:
        connected=is_connected()

        if connected:
            WebLauncher(argv[1])
        else:
            print("Unable to connect to internet ....")

    except ValueError:
        print("Error : Invalid datatype of input")
    
    except Exception as E:
        print("Error : Invalid type",E)



if __name__=="__main__":
    main()
