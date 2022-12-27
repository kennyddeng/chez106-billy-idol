import requests 
import json
import time

url = "https://player.rogersradio.ca/chez/widget/now_playing"
data = requests.get(url).json()

def lookForMusic():
    if (data["artist"] == "Billy Idol" and data["song_title"] == "White Wedding"):
        print("send sms")

def loop():
    while True:
        lookForMusic()
        time.sleep(30)


if __name__ == "__main__":
    loop()