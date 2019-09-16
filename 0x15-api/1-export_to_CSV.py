#!/usr/bin/python3

'''
Script for exporting employee data into CSV
'''

import csv
import requests
from sys import argv


def get_employee_tasks(user_id):
    '''Retrieves employees and tasks'''
    url = 'https://jsonplaceholder.typicode.com/'
    user_req = url + 'users/{}'.format(user_id)
    employee = requests.get(user_req).json()
    task_req = url + 'todos?userId={}'.format(employee.get('id'))
    tasks = requests.get(task_req).json()
    return {"employee": employee, "tasks": tasks}


def export_to_csv(data):
    with open('{}.csv'.format(argv[1]), mode='w') as _file:
        writer = csv.writer(_file, quoting=csv.QUOTE_ALL)
        e_id = data.get('employee').get('id')
        e_username = data.get('employee').get('username')
        for d in data.get('tasks'):
            writer.writerow([
                e_id,
                e_username,
                d.get('completed'),
                d.get('title')
                ])


if __name__ == '__main__':
    data = get_employee_tasks(argv[1])
    export_to_csv(data)
