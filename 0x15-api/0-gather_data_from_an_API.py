#!/usr/bin/python3

'''
Script for retrieving and printing employee tasks
'''

import requests
from sys import argv


def get_employee_tasks():
    '''Retrieves and prints completed employee tasks'''
    root_url = 'https://jsonplaceholder.typicode.com/'
    user_req = root_url + 'users/{}'.format(argv[1])
    employee = requests.get(user_req).json()
    employee_id = employee['id']
    task_req = root_url + 'todos?userId={}'.format(employee_id)
    tasks = requests.get(task_req).json()
    task_len = len(tasks)
    completed_tasks = [t for t in tasks if t['completed']]
    completed_len = len(completed_tasks)
    print('Employee {} is done with tasks({}/{}):'
          .format(employee['name'], completed_len, task_len))
    for task in completed_tasks:
        print('\t {}'.format(task['title']))


if __name__ == '__main__':
    get_employee_tasks()
