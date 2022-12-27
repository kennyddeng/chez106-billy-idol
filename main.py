import requests 
import json
import time
import keys
from twilio.rest import Client

client = Client(keys.account_sid, keys.auth_token)
message = client.messages.create(
    body="BILLY IDOL WHITE WEDDING - PLAYING NOW AT CHEZ106 - ITS A NICE DAY TO START AGAIN",
    from_=keys.twilio_number,
    to=keys.target_number
)

# chez106 webpage player
url = "https://player.rogersradio.ca/chez/widget/now_playing"
data = requests.get(url).json()

def sendSMS():
    print(message.body)

def lookForMusic():
    if (data["artist"] == "Billy Idol" and data["song_title"] == "White Wedding"):
        sendSMS()

def loop():
    while True:
        lookForMusic()
        time.sleep(30)

if __name__ == "__main__":
    loop()