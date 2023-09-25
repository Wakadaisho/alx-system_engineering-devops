#!/usr/bin/python3
"""
Get user and todo data from https://jsonplaceholder.typicode.com
and dump them to a JSON file
"""

import json
import requests
import sys


if __name__ == "__main__":
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}").json()
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos")
    todos = todos.json()

    with open('{}.json'.format(user['id']), 'w') as f:
        json.dump(
                {user['id']:
                 [{'task': i['title'],
                   'completed': i['completed'],
                   'username': user['username']}
                  for i in todos]}, f)
