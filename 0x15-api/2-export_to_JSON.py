#!/usr/bin/python3
""" python script that uses API to get user data and output json file
"""

import csv
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    userid = sys.argv[1]
    user = '{}users/{}'.format(url, userid)
    res = requests.get(user)
    json_o = res.json()
    name = json_o.get('username')

    todos = '{}todos?userId={}'.format(url, userid)
    res = requests.get(todos)
    tasks = res.json()
    l_task = []
    for task in tasks:
        dict_tasks = {"task": task.get('title'),
                      "completed": task.get('completed'),
                     "username": name}
        l_task.append(dict_tasks)


        dic_t = {str(userid): l_task}
        fileName = f'{userid}.json'
        with open(fileName, mode='w') as j:
            json.dump(dic_t, j)
print(f"Data has been successfully saved to {fileName}.")
