#!/usr/bin/python3
"""gets the subscribers from reddit api"""
from requests import get


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'user'}
    Rdict = get(url, headers=headers, allow_redirects=False)
    if Rdict.status_code is not 200:
        return 0
    else:
        data = Rdict.json().get('data')
        sub = data.get('subscribers')
        return sub
