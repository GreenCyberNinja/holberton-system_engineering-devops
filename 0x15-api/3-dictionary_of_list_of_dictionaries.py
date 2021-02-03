#!/usr/bin/python3
"""gets from api and returns information about his/her TODO list progress"""

from requests import get
import json

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    usernames = get(url + '/users/').json()
    userdict = {}
    for user in usernames:
        username = get(url + '/users/' +
                       str(user["id"])).json().get('username')
        tasks = get(url + '/users/' + str(user["id"]) + '/todos').json()
        tasklist = []
        for task in tasks:
            taskdict = {}
            taskdict["task"] = task.get('title')
            taskdict["completed"] = task.get('completed')
            taskdict["username"] = "{}".format(username)
            tasklist.append(taskdict)
        userdict[str(user["id"])] = tasklist
    with open('todo_all_employees.json', 'w') as jsonfile:
        jsonfile.write(json.dumps(userdict))
