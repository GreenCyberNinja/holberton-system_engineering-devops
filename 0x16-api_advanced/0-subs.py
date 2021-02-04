#!/usr/bin/python3
"""gets the subscribers from reddit api"""
from requests import get


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'user',}
    try:
        Rdict = get(url, headers=headers, allow_redirects=False).json()
    except(ValueError):
        return 0;
    data = Rdict.get('data')
    sub = data.get('subscribers')
    if sub == None:
        sub = 0;
    return sub
