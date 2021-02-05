#!/usr/bin/python3
"""gets the subscribers from reddit api"""
from requests import get


def recurse(subreddit, hot_list=[], after=''):
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {'user-agent': 'user'}
    Rdict = get(url, headers=headers,
                params={'after': after},
                allow_redirects=False)
    if Rdict.status_code is not 200:
        return('None')
    else:
        data = Rdict.json().get('data').get('children')
        for title in data:
            hot_list.append(title.get('data').get('title'))
        after = Rdict.json().get('data').get('after')
        if after:
            recurse(subreddit, hot_list, after)
        return hot_list
