#!/usr/bin/python3
""" queries the Reddit API """
import requests import get


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit
    """
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    agent = {"User-Agent": "MyCoolReqName/1.0 (by /u/ReplyAdventurous5909)"}

    resp = get(url, headers=agent)
    if resp.status_code == 200:
        top = resp.json()
        if "data" in top and "children" in top["data"]:
            for t in top["data"]["children"]:
                ten = t["data"]["title"]
                print(ten)
    else:
        print(None)
