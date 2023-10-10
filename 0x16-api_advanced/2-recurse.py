#!/usr/bin/python3
"""
Return all hot article titles in a subreddit
"""
import requests


def recurse(subreddit, hot_list=[],
            pagination={"after": "", "count": 0}):
    """
    Return all hot article titles in a subreddit

    Args:
        subreddit (str): subreddit to query
        hot_list (list): list of currently found subreddits
    """
    headers = {"User-Agent":
               "python3.4/requests:v2.31.0 (by /u/Wakadaisho)"}
    res = requests.get("https://www.reddit.com/r/{}.json?after={}&count={}"
                       .format(subreddit,
                               pagination.get("after", ""),
                               pagination.get("count", "")),
                       headers=headers,
                       allow_redirects=False)
    try:
        json = res.json()
        hot_list += [post['data']['title']
                     for post in json['data']['children']]
        if not json['data']['after']:
            if len(hot_list):
                return hot_list
            return None
        else:
            return recurse(subreddit,
                           hot_list=hot_list,
                           pagination={"after": json['data']['after'],
                                       "count": (json['data']['dist'] +
                                                 pagination.get("count"))})
    except Exception:
        return None
