#!/usr/bin/python3
'''
Gathers and processes data from a REST API
'''
import requests
import sys

if __name__ == "__main__":
    '''
    finds, formats, outputs data from api
    '''
    todos_done_list = []
    todos_count = 0
    employee_id = int(sys.argv[1])
    employees = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(employee_id))
    name = employees.json()['name']
    all_tasks = requests.get(
                'https://jsonplaceholder.typicode.com/todos?userId={}'
                .format(employee_id))
    task_list = all_tasks.json()

    todos_count = len(task_list)
    for task in task_list:
        if task.get('completed') is True:
            todos_done_list.append(task.get('title'))
        todos_done = len(todos_done_list)
    print('Employee {} is done with tasks({}/{}):'
          .format(name, todos_done, todos_count))
    for item in todos_done_list:
        print('\t {}'.format(item))
