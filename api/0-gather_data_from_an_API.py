#!/usr/bin/python3
""" getting todo list of users from an api  """

import sys
import requests


n = sys.argv[1]
resUser = requests.get(f'https://jsonplaceholder.typicode.com/users/{n}')
response = resUser.json()
resTask = requests.get('https://jsonplaceholder.typicode.com/todos')
responseTask = resTask.json()
done = 0
total = 0
doneTask = []
for task in responseTask:
    if task["userId"] == int(n):
        if task["completed"] is True:
            doneTask.append(task["title"])
            done += 1
        else:
            total += 1

total += done

print(f"Employee {response['name']} is done with task({done}/{total})")
for task in doneTask:
    print(f"\t {task}")

if __name__ == "__main__":
    """ getting todo list of users from an api  """
