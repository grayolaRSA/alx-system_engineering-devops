#!/usr/bin/python3
"""
Python script that uses an API
 to get all user data and output it to a JSON file.
"""

import csv
import json
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    users_url = f'{url}users'
    res = requests.get(users_url)
    users = res.json()
    dic_t = {}
    userids = [user['id'] for user in users]
    for userid in userids:
        user_url = f'{url}users/{userid}'
        res = requests.get(user_url)
        json_o = res.json()
        name = json_o.get('username')

        todos = f'{url}todos?userId={userid}'
        res = requests.get(todos)
        tasks = res.json()
        l_task = []
        for task in tasks:
            dict_tasks = {"username": name,
                          "task": task.get('title'),
                          "completed": task.get('completed')}
            l_task.append(dict_tasks)

        dic_t[str(userid)] = l_task

    fileName = 'todo_all_employees.json'
    with open(fileName, mode='w') as j:
        json.dump(dic_t, j)
