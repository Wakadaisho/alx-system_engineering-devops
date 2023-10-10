#!/usr/bin/python3
"""
Return number of subscribers in a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Return number of subscribers in a subreddit

    Args:
        subreddit (str): subreddit to query
    """
    headers = {"User-Agent":
               "python3.4/requests:v2.31.0 (by /u/Wakadaisho)"}
    res = requests.get("https://www.reddit.com/r/{}/about.json"
                       .format(subreddit),
                       headers=headers,
                       allow_redirects=False)
    try:
        json = res.json()
        return json['data']['subscribers']
    except Exception:
        return 0
