#!/usr/bin/python3
"""gets the subscribers from reddit api"""
from requests import get


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'user'}
    Rdict = get(url, headers=headers).json()
    data = Rdict.get('data')
    return (data.get('subscribers'))
