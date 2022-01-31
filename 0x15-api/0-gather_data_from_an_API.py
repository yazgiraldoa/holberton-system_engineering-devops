#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys

if __name__ == '__main__':
    id = sys.argv[1]
    users_url = "https://jsonplaceholder.typicode.com/users/"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    name = requests.get(users_url + id).json().get("name")
    tasks = requests.get(todos_url + '?userId=' + id).json()
    tasks_completed = requests.get(todos_url +
                                   '?completed=true&userId=' + id).json()

    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(tasks_completed), len(tasks)))
    for task in tasks_completed:
        print("\t {}".format(task.get("title")))
