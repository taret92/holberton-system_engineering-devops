#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    name_user = '{}users/{}'.format(url, sys.argv[1])
    r = requests.get(name_user)
    r_json = r.json()
    print("Employee {} is done with tasks".format(r_json.get('name')), end="")
    r = requests.get(url + 'all', params={'userId': sys.argv[1]})
    tasks = r.json()
    task_list = []
    for task in tasks:
        if task.get('completed'):
            task_list.append(task)

    print("({}/{}):".format(len(task_list), len(tasks)))
    for task in task_list:
        print("\t {}".format(task.get("title")))
