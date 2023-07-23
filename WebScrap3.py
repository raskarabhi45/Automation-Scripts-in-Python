# Link extractor using Web scrapping

import os 
import bs4
import requests
from sys import *

def MarvellousLinksDisplay(URL):
    res=requests.get(URL)
    print(type(res))

    soup=bs4.BeautifulSoup(res.text,'lxml')
    print(type(soup))

    links=soup.findAll('a',href=True)

    return links

def main():
    print("Marvellous Infosystems by Piyush Khairnar")

    print("Application name : "+argv[0])

    if(len(argv)==2):
        if(argv[1]=="-h") or (argv[1]=="-H"):
            print(" This script is used to fetch links from wikipedia file")
            exit()

        if(argv[1]=="-u") or (argv[1]=="-U"):
            print(" usage : ApplicationName")
            exit()

    url="https://en.wikipedia.org/wiki/Python_(programming_language)"

    arr=MarvellousLinksDisplay(url)

    print("Links are")

    for element in arr:
        if "#" not in element['href']:
            print(element['href'])
            print()

    
if __name__=="__main__":
    main()