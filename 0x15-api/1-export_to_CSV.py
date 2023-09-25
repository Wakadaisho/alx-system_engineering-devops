#!/usr/bin/python3
"""
Get user and todo data from https://jsonplaceholder.typicode.com
and save them to a CSV file
"""

import csv
import requests
import sys


if __name__ == "__main__":
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}").json()
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos")
    todos = todos.json()

    with open('{}.csv'.format(user['id']), 'w') as f:
        csv_file = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            csv_file.writerow(
                    (user['id'],
                     user['username'],
                     task['completed'],
                     task['title']
                     ))
