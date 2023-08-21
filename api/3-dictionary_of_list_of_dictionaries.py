#!/usr/bin/python3
""" getting todo list of users from an api  """

import json
import requests


if __name__ == "__main__":
    """ getting todo list of users from an api  """
    resUser = requests.get('https://jsonplaceholder.typicode.com/users')
    response = resUser.json()
    resTask = requests.get('https://jsonplaceholder.typicode.com/todos')
    responseTask = resTask.json()

    json_file = "todo_all_employees.json"
    task_list = []
    eache_usr = []
    all_users = []
    for user in response:
        a_user = []
        USER_ID = int(user["id"])
        for task in responseTask:
            if int(task["userId"]) == USER_ID:
                TASK_TITLE = task['title']
                TASK_COMPLETED_STATUS = task["completed"]
                USERNAME = user["username"]

                task_list.append({
                    "task": TASK_TITLE,
                    "completed": TASK_COMPLETED_STATUS,
                    "username": USERNAME
                })
                a_user.append({USER_ID: task_list})
        all_users.append(a_user)
    with open(json_file, "w") as jf:
        json.dump(all_users, jf)
