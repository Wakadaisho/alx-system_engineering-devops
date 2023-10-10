#!/usr/bin/python3
"""
Return top ten articles in a subreddit
"""
import requests


def top_ten(subreddit):
    """
    Return top ten articles in a subreddit

    Args:
        subreddit (str): subreddit to query
    """
    headers = {"User-Agent":
               "python3.4/requests:v2.31.0 (by /u/Wakadaisho)"}
    res = requests.get("https://www.reddit.com/r/{}/hot.json"
                       .format(subreddit),
                       headers=headers,
                       allow_redirects=False)
    try:
        json = res.json()
        print("\n".join([post['data']['title']
                         for post in json['data']['children'][:10]]))
    except Exception:
        print(None)
