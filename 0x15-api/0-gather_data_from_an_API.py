#!/usr/bin/python3
"""gets from api and returns information about his/her TODO list progress"""

import requests
from sys import argv


if __name__ == "__main__":
    """displays completed tasks"""
    TOTAL_NUMBER_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0
    TASKS = []
    empid = argv[1]
    empurl = 'https://jsonplaceholder.typicode.com/users/{}'\
        .format(int(empid))
    EMPLOYEE_NAME = requests.get(empurl).json()
    print("Employee {} is done with tasks"
          .format(EMPLOYEE_NAME.get('name')), end="")
    todourl = ("https://jsonplaceholder.typicode.com/todos")
    urlreq = requests.get(todourl).json()
    for toto in urlreq:
        if toto.get('userId') == int(empid):
            TOTAL_NUMBER_OF_TASKS += 1
            if toto.get('completed') is True:
                NUMBER_OF_DONE_TASKS += 1
                TASKS.append(toto.get("title"))
    print('{}/{}):'.format(NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for TASK_TITLE in TASKS:
        print('\t {}'.format(TASK_TITLE))
