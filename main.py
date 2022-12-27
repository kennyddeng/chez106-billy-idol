import requests 
import json
import time

import config
import keys

from twilio.rest import Client

client = Client(keys.account_sid, keys.auth_token)
message = client.messages.create(
    body=config.message,
    from_=keys.twilio_number,
    to=keys.target_number
)

url = config.url
data = requests.get(url).json()

def sendSMS():
    print(message.body)

def lookForMusic():
    if (data["artist"] == config.artist and data["song_title"] == config.song):
        sendSMS()

def loop():
    while True:
        lookForMusic()
        time.sleep(config.sample_time)

if __name__ == "__main__":
    loop()