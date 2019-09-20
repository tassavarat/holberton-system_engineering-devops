#!/usr/bin/python3
"""2-recurse module"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Return: List containing titles of all hot articles for given subreddit
    None if no results found
    """
    r = requests.get("https://reddit.com/r/{}/hot.json?after={}".
                     format(subreddit, after),
                     headers={"User-agent": "custom"})

    if r.status_code != 200:
        return None
    after = r.json().get("data").get("after")
    if not r.json().get("data").get("after"):
        return hot_list

    hot_list.append(r.json().get("data").get("children")[0].get("data").
                    get("title"))
    recurse(subreddit, hot_list, after)
    return hot_list
