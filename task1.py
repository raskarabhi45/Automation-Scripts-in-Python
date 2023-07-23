# Automation in python
# Task scheduler 
# display hello world after every minute 
# templete for automation

import schedule  #ModuleNotFoundError: No module named 'schedule'
import time
import datetime

#logic should be here in this method
def fun():
    print("Inside fun")

def main():
    print("Inside Task schedular")

    schedule.every(1).minutes.do(fun)  

    while(True): #unconditional infinite true
        schedule.run_pending()
        #same like lahan mulana zopvlyavr aaila tichi kame krta yetat   
        time.sleep(1)  #for third time our program stops and after wakeup it check whetehr there is any task for him or not
   

if __name__=="__main__":
    main()