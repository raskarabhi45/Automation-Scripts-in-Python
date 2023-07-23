
import schedule  
import time
import datetime

def task_minute():
    print("task based on minutes gets scheduled at : ",datetime.datetime.now())

def task_hour():
    print("task based on hours gets scheduled at : ",datetime.datetime.now())

def task_day():
    print("task based on days gets scheduled at : ",datetime.datetime.now())

#script terminator  function
#to abbort our application using exit
#i=0
#increment in any upper function i=i+1
# and sys.exit()

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