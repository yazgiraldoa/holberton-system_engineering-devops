#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""
import csv
import requests
import sys

if __name__ == '__main__':
    id = sys.argv[1]
    users_url = "https://jsonplaceholder.typicode.com/users/"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    username = requests.get(users_url + id).json().get("username")
    tasks = requests.get(todos_url + '?userId=' + id).json()

    with open(id + '.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            csvwriter.writerow([id] + [username] + [task.get('completed')] +
                               [task.get('title')])
