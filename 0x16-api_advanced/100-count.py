#!/usr/bin/python3
"""
Return word count of keywords in the titles of all hot articles
"""
import re
import requests


def count_words(subreddit, word_list,
                count={}, pagination={"after": "", "count": 0}):
    """
    Return word count of keywords in the titles of all hot articles

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
    if type(word_list) == list:
        word_list = set([w.lower() for w in word_list])
    try:
        json = res.json()
        titles = " ".join([post['data']['title']
                           for post in json['data']['children']])
        for w in word_list:
            matches = len(re.findall(r"\b{}\b".format(w), titles, re.I))
            if matches:
                count[w] = (count.get(w, 0) + matches)
        if not json['data']['after']:
            for k, v in sorted(count.items(), key=lambda x: (-x[1], x[0])):
                print("{}: {}".format(k, v))
        else:
            return count_words(subreddit,
                               word_list=word_list,
                               count=count,
                               pagination={"after": json['data']['after'],
                                           "count": (json['data']['dist'] +
                                                     pagination.get("count"))})
    except Exception:
        pass
