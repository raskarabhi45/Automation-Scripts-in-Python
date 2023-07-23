#Aoto Downloader
# """C:\Users\ABHIJEET\Desktop\Python\Automation>python AutoDownloader.py C:\Users\ABHIJEET\Desktop\Python\Automation\img
# ------Marvellous Infosystems by Piyush Khairnar-----
# Application name : AutoDownloader.py
# File successfully Download"""

#Automation script which downloads specific file and stote into the current directory of application

import os
import requests
from sys import *
from urllib.parse import urlparse

def is_downloadable(url):
    h=requests.head(url,allow_redirects=True)
    header=h.headers
    content_type=header.get('content-type')

    if 'text' in content_type.lower():
        return False
    
    if 'html' in content_type.lower():
        return False
    return True

def get_filename_from_cd(cd):
    a=urlparse(cd)
    return os.path.basename(a.path)

def MarvellousDownload(url):
    allowed=is_downloadable(url)

    if allowed:
        try:
            res=requests.get(url,allow_redirects=True)
            res.raise_for_status()
            filename=get_filename_from_cd(url)
            fd=open(filename,"wb")

            for buffer in res.iter_content(1024):
                fd.write(buffer)

            fd.close()
            return True
        except Exception as E:
            return False
    
    else:
        return False


def main():
    print("------Marvellous Infosystems by Piyush Khairnar-----")

    print("Application name : "+argv[0])

    if(len(argv)!=2):
        print("Error: Invalid number of argumets")
        exit()

    if(argv[1]=="-h") or (argv[1]=="-H"):
        print("This scrip is used to download file")
        exit()

    if(argv[1]=="-u") or (argv[1]=="-U"):
        print("usage : Application_name Absolute_path_of_Directory_Extention")
        exit()

    url='https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_960_720.jpg'

    result=MarvellousDownload(url)

    if result:
        print("File successfully Download")
    else:
        print("Failed to download")


if __name__=="__main__":
    main()