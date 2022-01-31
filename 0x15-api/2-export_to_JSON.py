#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
import json
import requests
import sys

if __name__ == '__main__':
    id = sys.argv[1]
    users_url = "https://jsonplaceholder.typicode.com/users/"
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    username = requests.get(users_url + id).json().get("username")
    tasks = requests.get(todos_url + '?userId=' + id).json()

    tasks_list = []
    json_to_save = {}
    for task in tasks:
        task_dict = {}
        task_dict['task'] = task.get("title")
        task_dict['completed'] = task.get("completed")
        task_dict['username'] = username
        tasks_list.append(task_dict)
    json_to_save[id] = tasks_list

    with open(id + '.json', 'w') as json_file:
        json.dump(json_to_save, json_file)
