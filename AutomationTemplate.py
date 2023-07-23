#### Python mdheeee sgl krtaaa yettttt that is anything you want you can do it in python
#Automation scripts template
#using command line arguments
#python AutomationTemplate.py -h
from sys import *
from os import *

def Script_Task(no):
    if(no%2==0):
        print("It is even number")
    else:
        print("It is odd number")



def main():
    print("---------- Marvellous Infosystems Automations ------------")

    print("Automation script started with name : ",argv[0])

    if(len(argv)!=2):
        print("Error : Insufficinet Arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

    if(argv[1]=="-h") or (argv[1]=="-H"):
        print("Help : This script is used to perform _______________")
        exit()

    elif((argv[1]=="-u") or (argv[1]=="-U")):
        print("Usage : Provide  _____ number of arguments as ")
        print("First argument as :______")
        print("Second Argument as :______")
        exit()

    else:
        Script_Task(int(argv[1]))

    

if __name__=="__main__":
    main()