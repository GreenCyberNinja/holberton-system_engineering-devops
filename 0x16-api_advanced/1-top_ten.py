#!/usr/bin/python3
"""gets the subscribers from reddit api"""
from requests import get


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot/.json?count=1".format(subreddit)
    headers = {'user-agent': 'user'}
    rdict = get(url, headers=headers, allow_redirects=False)
    if rdict.status_code is not 200:
        print('None')
    else:
        data = rdict.json().get('data').get('children')
        count = 0
        while count < 10:
            subdata = data[count].get('data').get('title')
            print(subdata)
            count += 1
