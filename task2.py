
# display hello world after every minute 
import schedule  
import time
import datetime

#logic schould be here in this method
def fun():
    print("Inside fun at the time ",datetime.datetime.now()) 

def main():
    print("Inside Task schedular")
    print("Current time is : ",datetime.datetime.now())

    schedule.every(1).minutes.do(fun)

    while(True): #unconditional infinite true
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()