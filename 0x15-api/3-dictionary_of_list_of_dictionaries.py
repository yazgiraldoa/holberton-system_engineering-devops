#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
import json
import requests
import sys

if __name__ == '__main__':
    users_url = "https://jsonplaceholder.typicode.com/users/"
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users = requests.get(users_url).json()

    json_to_save = {}
    for user in users:
        id = user.get('id')
        tasks = requests.get(todos_url + '?userId=' + str(id)).json()

        tasks_list = []
        for task in tasks:
            task_dict = {}
            task_dict['task'] = task.get("title")
            task_dict['completed'] = task.get("completed")
            task_dict['username'] = user.get("username")
            tasks_list.append(task_dict)
        json_to_save[id] = tasks_list

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(json_to_save, json_file)
