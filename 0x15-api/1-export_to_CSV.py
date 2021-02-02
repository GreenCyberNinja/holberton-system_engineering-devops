#!/usr/bin/python3
"""gets from api and returns information about his/her TODO list progress"""

from requests import get
from sys import argv
import csv

if __name__ == "__main__":
    """displays completed tasks"""
    empid = argv[1]
    userurl = 'https://jsonplaceholder.typicode.com/users/' + empid
    todourl = 'https://jsonplaceholder.typicode.com/todos?userId=' + empid
    users = get(userurl).json()
    toto = get(todourl)
    FILE = "{}.csv".format(argv[1])

    with open(FILE, mode='w+', newline='') as cvs:
        ghost_writer = csv.writer(cvs, delimiter=',', quotechar='"',
                                  quoting=csv.QUOTE_ALL)
        TASKS = []
        for to in toto.json():
            TASKS.append(users.get("id"))
            TASKS.append(users.get("username"))
            TASKS.append(users.get("completed"))
            TASKS.append(users.get("title"))
            ghost_writer.writerow(TASKS)
            TASKS = []
