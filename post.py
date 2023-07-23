# Install instabot library using pip
# pip install instabot

import os
import random
import schedule
import time
from instabot import Bot

# Replace these with your actual Instagram credentials
USERNAME = "_refreshing_thoughts"
PASSWORD = "Abhi@123"

# Replace this with the path to the file containing your thoughts
# THOUGHTS_FILE = "path/to/your/thoughts_file.txt"

# Initialize the Instagram bot
bot = Bot()

def login():
    bot.login(username=USERNAME, password=PASSWORD)

# def read_thoughts():
#     with open(THOUGHTS_FILE, "r") as file:
#         thoughts = file.readlines()
#     return thoughts

def create_post():
    # Assuming you have images related to each thought with filenames like "thought_1.jpg", "thought_2.jpg", etc.
    # Adjust the path accordingly.
    image_path = f"C:\\Users\\ABHIJEET\\Pictures\\Screenshots{random.randint(1, 5)}.jpg"


    # Upload the post with the thought as the caption
    bot.upload_photo(image_path)

def post_thoughts():

        create_post()
        # Add some delay before posting the next thought (adjust as needed)
        time.sleep(random.randint(600, 1200))  # Random delay between 10 to 20 minutes

if __name__ == "__main__":
    login()

    # Schedule the posting to run daily at a specific time (adjust as needed)
    schedule.every().day.at("14:12").do(post_thoughts)

    while True:
        schedule.run_pending()
        time.sleep(1)
