#!/usr/bin/python3
"""gets from api and returns information about his/her TODO list progress"""

from requests import get
from sys import argv
import json

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    username = get(url + '/users/' + argv[1]).json().get('username')
    tasks = get(url + '/users/' + argv[1] + '/todos').json()
    tasklist = []
    for task in tasks:
        taskdict = {}
        taskdict["task"] = task.get('title')
        taskdict["completed"] = task.get('completed')
        taskdict["username"] = "{}".format(username)
        tasklist.append(taskdict)
    userdict = {argv[1]: tasklist}
    with open('{}.json'.format(argv[1]), 'w') as jsonfile:
        jsonfile.write(json.dumps(userdict))
