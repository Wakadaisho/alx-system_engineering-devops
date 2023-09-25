#!/usr/bin/python3
"""
Get user todo data from https://jsonplaceholder.typicode.com
and display the ratio of tasks a user as done
"""

import requests
import sys


if __name__ == "__main__":
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}").json()
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos")
    todos = todos.json()

    done_tasks = [i for i in todos if i['completed']]

    print("Employee {} is done with tasks({}/{}):".format(
        user['name'],
        len(done_tasks),
        len(todos)))
    for i in done_tasks:
        print(f"\t {i['title']}")
