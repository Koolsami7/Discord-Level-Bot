import requests
import hashlib
import random
from random import randint
import time

# EDIT BELOW HERE

authToken = "DISCORD AUTH TOKEN"

fingerprint = "DISCORD FINGERPRINT"

words = ["hi", "bye", ":snail:"]

servers = []
servers.append({'name':'Discord Server', 'server':'Server ID','channel':'Channel ID'})

# DO NOT TOUCH ANYTHING BELOW HERE

def domsg(m,server,channel):
    url = "https://discordapp.com/api/v6/channels/"+channel+"/messages"
    
    payload = "{\"content\":\"" + m + "\",\"nonce\":\""+str(randint(500000000000000000,599999999999999999)) + "\",\"tts\":false}"
    
    headers = {
    'x-super-properties': "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzEzXzYpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS82OS4wLjM0OTcuMTAwIFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiI2OS4wLjM0OTcuMTAwIiwib3NfdmVyc2lvbiI6IjEwLjEzLjYiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjY5MDIsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",
    'x-fingerprint': fingerprint,
    'accept-language': "en-US",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    'content-type': "application/json",
    'authorization': authToken,
    'origin': "https://discordapp.com",
    'accept': "*/*",
    'referer': "https://discordapp.com/channels/"+server+"/"+channel,
    'accept-encoding': "gzip, deflate, br",
    'cookie': "__cfduid=d1e6c16ab080a7b90e3f8f0206a2eb7747cf63c3522; locale=en-US",
    'cache-control': "no-cache"
    }
    
    requests.request("POST", url, data=payload, headers=headers)

while True:
    msg = random.choice(words)
    print("Message '{}' sending to {} server(s)".format(msg, len(servers)))
    
    for s in servers:
        domsg(msg,s['server'],s['channel'])
        print("Sent to: {}".format(s['name']))
        waittime = randint(2,4)
        print("waiting {}s...".format(waittime))
        time.sleep(waittime)
        
    nextsend = randint(200,550)
    print("Sending next message(s) in: {} seconds".format(nextsend))
    time.sleep(nextsend)
