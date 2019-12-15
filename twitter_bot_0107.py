# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 20:09:17 2019

@author: rahul
"""

import tweepy

from keys import *

import time

import re

print(CONSUMER_KEY)
print(CONSUMER_SECRET)
print(ACCESS_KEY)
print(ACCESS_SECRET)

print("tweepy imported")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

print("auth done")

auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

print("access given")

api = tweepy.API(auth, wait_on_rate_limit=True)


print(api)

print("api created")

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    #print(type(f_read.read().strip()))
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name , 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets(fn):
    print('retrieving and replying to tweets...', flush=True)
    last_seen_id = retrieve_last_seen_id(fn)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode ='extended')
    for mentions in reversed(mentions):
        id = mentions.id
        usr = mentions.user.screen_name
        store_last_seen_id(id, fn)
        if '#hellowhatsup' in mentions.full_text.lower(): 
            print("question asked")
            print('responding')
            api.update_status(f'@{usr} Hi, I am good, thanks! How about you?' , id)


while 1:
    reply_to_tweets(FILE_NAME)
    time.sleep(15)

#print(api.mentions_timeline().__dict__.keys())


#print(mentions[0].__dict__.keys())

#print(mentions[0].text)
#print(mentions[0].id)

    
        





    
    
    





