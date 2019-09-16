#!/usr/bin/python3

'''
Script for retrieving and printing employee tasks
'''

import requests
from sys import argv


def get_employee_tasks(user_id):
    '''Retrieves employees and tasks'''
    root_url = 'https://jsonplaceholder.typicode.com/'
    user_req = root_url + 'users/{}'.format(user_id)
    employee = requests.get(user_req).json()
    employee_id = employee.get('id')
    task_req = root_url + 'todos?userId={}'.format(employee_id)
    tasks = requests.get(task_req).json()
    return {"employee": employee, "tasks": tasks}


def print_completed_tasks(data):
    task_len = len(data.get('tasks'))
    completed_tasks = [t for t in data.get('tasks') if t.get('completed')]
    completed_len = len(completed_tasks)
    print('Employee {} is done with tasks({}/{}):'
          .format(data.get('employee').get('name'), completed_len, task_len))
    for task in completed_tasks:
        print('\t {}'.format(task.get('title')))


if __name__ == '__main__':
    data = get_employee_tasks(argv[1])
    print_completed_tasks(data)
