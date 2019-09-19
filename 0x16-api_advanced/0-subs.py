#!/usr/bin/python3
"""Queries Reddit API
Return: Number of subcribers for given subreddit
0 if invalid subreddit
"""
import requests


def number_of_subscribers(subreddit):
    r = requests.get("https://reddit.com/r/{}/about.json".format(subreddit),
                     headers={"User-agent": "custom"})
    if(r.status_code == 200):
        return r.json().get("data").get("subscribers")
    return 0
