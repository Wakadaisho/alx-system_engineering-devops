#!/usr/bin/python3
"""
Get all user and todo data from https://jsonplaceholder.typicode.com
and dump them to a JSON file
"""

import json
import requests
import sys


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    records = {}

    for user in users:
        todos = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{user['id']}/todos")
        records.update({user['id']:
                        [{'username': user['username'],
                          'task': i['title'],
                          'completed': i['completed']}
                         for i in todos.json()]})

    with open('todo_all_employees.json', 'w') as f:
        json.dump(records, f)
