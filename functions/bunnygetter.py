import ctypes
import praw
import random
import requests
from urllib.request import urlretrieve
import sys, os 
import json
import re

def load_config(config_file_path):
    data = {}
    with open(config_file_path, "r") as file:
        data=json.load(file)
    return data


def update_bunny():

    data = load_config('static/config.json')

    r = praw.Reddit(
        
        client_id=data['clientid'],
        client_secret=data['clientsecret'],
        user_agent="user_agent",
        username=data['reddituname'],
        password=data['redditpass'],
        check_for_updates=False,
        comment_kind="t1",
        message_kind="t4",
        redditor_kind="t2",
        submission_kind="t3",
        subreddit_kind="t5",
        trophy_kind="t6",
        oauth_url="https://oauth.reddit.com",
        reddit_url="https://www.reddit.com",
        short_url="https://redd.it",
        )


    subreddit = r.subreddit("aww") # subreddit
    radpics = subreddit.search("bunny", sort='hot', syntax='lucene', time_filter='month')

    urls = []
    for pic in radpics:
        search = re.search(r'^.*\.jpg$', pic.url)
        if search != None:
            urls.append(pic.url)  # gather list of post urls
    
    
    data= {}
    data['urls'] = []
    with open("static/bunny_urls.json", "w") as file:
        for url in urls:
            data['urls'].append(url)
        file.write(json.dumps(data))


def get_bunny():
    data= {}
    with open("static/bunny_urls.json", "r") as file:
        data=json.load(file)
    url =data['urls'][random.randint(0, len(data['urls'])-1)]



    urlretrieve(url,  "static/bunny.jpg")

# update_bunny()
    