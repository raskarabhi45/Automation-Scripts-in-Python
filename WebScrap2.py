from bs4 import *
import requests
import os

def folder_create(images):
    try:
        folder_name=input("Enter folder name : ")
        os.mkdir(folder_name)

    except:
        print("Folder exist with that name !!")
        folder_create()

    download_images(images,folder_name)


def download_images(images,folder_name):
    cnt=0

    print(f"Total {len(images)} Image Found !")

    if len(images)!=0:
        for i,image in enumerate(images):
            try:
                image_link=image["data-srcset"]

            except:
                try:
                    image_link=image["data-fallback-src"]
                except:
                    try:
                        image_link=image["src"]
                    
                    except:
                        pass

                
#https://www.pexels.com/photo/green-and-blue-peacock-feather-674010/
            try:
                r=requests.get(image_link).content
                try:
                    r=str(r,'utf-8')

                except UnicodeDecodeError:
                    with open(f"{folder_name}/images{i+1}.jpg","wb+") as f:
                        f.write(r)
                    
                    cnt=cnt+1
            except:
                pass

        if cnt==len(images):
            print("All Images Downloaded !!")

        else:
            print(f"Total {cnt} Images Downloaded out of {len(images)}")

def main():
    print("-Marvellous Infosystems by Piyush Khairnar")

    print("Application name : Auto image downloader")

    url=input("Enter URL from where you want to download images :")

    r=requests.get(url)

    soup=BeautifulSoup(r.text,'html.parser')

    images=soup.findAll('img')

    folder_create(images)

if __name__=="__main__":
    main()