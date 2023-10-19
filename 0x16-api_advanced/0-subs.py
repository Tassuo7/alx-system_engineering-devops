#!/usr/bin/python3
""" queries the Reddit API """
import requests import get


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers for a given subreddit
    """
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyCoolReqName/1.0 (by /u/ReplyAdventurous5909)"}
    resp = get(url, headers=headers)
    if resp.status_code == 200:
        ret = resp.json()
        return ret["data"]["subscribers"]
    else:
        return 0
