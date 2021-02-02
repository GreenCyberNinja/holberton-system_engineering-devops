#!/usr/bin/python3
"""gets from api and returns information about his/her TODO list progress"""

from requests import get
from sys import argv
import json

if __name__ == "__main__":
    """displays completed tasks"""
    empid = argv[1]
    userurl = 'https://jsonplaceholder.typicode.com/users/' + empid
    todourl = 'https://jsonplaceholder.typicode.com/todos?userId=' + empid
    users = get(userurl).json()
    numof_tsk = get(todourl).json()
    name = users.get("username")
    ans = {}
    tasks = []
    for toto in numof_tsk:
        dictask = {}
        dictask["username"] = str(name)
        dictask["completed"] = toto.get("completed")
        dictask["task"] = str(toto.get("title"))
        tasks.append(dictask)
    ans.update({users.get(id): tasks})
    file_name = "{}.json".format(empid)
    with open(file_name, mode='w+', newline='') as jsonfile:
        jsonfile.write(json.dumps(ans))
