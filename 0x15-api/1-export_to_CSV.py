#!/usr/bin/python3
"""gets from api and returns information about his/her TODO list progress"""

from requests import get
from sys import argv
import csv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    username = get(url + '/users/' + argv[1]).json().get('username')
    tasks = get(url + '/users/' + argv[1] + '/todos').json()

    with open('{}.csv'.format(argv[1]), 'w+') as csvfile:
        ghst_wrtr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            line = []
            line.append(argv[1])
            line.append(username)
            line.append(task.get('completed'))
            line.append(task.get('title'))
            ghst_wrtr.writerow(line)
