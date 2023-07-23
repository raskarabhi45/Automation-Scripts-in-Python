
# display hello world after every minute 
#to terminate the application automatically
import schedule  
import time
import datetime
import sys

i=0

def task_minute():
    print("task based on minutes gets scheduled at : ",datetime.datetime.now())
    i=i+1
    if(i==3):
        exit()

def task_hour():
    print("task based on hours gets scheduled at : ",datetime.datetime.now())

def task_day():
    print("task based on days gets scheduled at : ",datetime.datetime.now())



def main():
    print("Inside Task schedular")
    print("Current time is : ",datetime.datetime.now())

    schedule.every(1).minutes.do(task_minute)
    schedule.every(1).hour.do(task_hour)
    schedule.every(1).saturday.at("18:00").do(task_day)
    

    while(True): #unconditional infinite true
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()