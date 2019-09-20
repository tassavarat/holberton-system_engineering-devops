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
        # print("status code not 200")
        return None
    after = r.json().get("data").get("children")[0].get("data").get("name")
    # print("after is", after)
    if not r.json().get("data").get("children")[0].get("data").get("name"):
        # print("in base case")
        return hot_list

    hot_list.append(r.json().get("data").get("children")[0].get("data").
                    get("title"))
    # print("recursing")
    recurse(subreddit, hot_list, after)
    # print("hot_list is", hot_list)
    return hot_list


'''
    while r.json().get("data").get("children")[0].get("data").get("after"):
        r = requests.get("https://reddit.com/r/{}/hot.json?after={}".
                         format(subreddit, r.json().get("data").get("children")[0].get("data").get("name")), headers={"User-agent": "custom"})
        hot_list.append(r.json().get("data").get("children")[0].get("data").get("title"))
        print(hot_list)
    print("####")
    print(r.json().get("data").get("children")[2].get("data").get("title"))
    print("####")
'''
