#!/usr/bin/python3

'''
Script for exporting employee data into CSV
'''

import csv
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


def export_to_csv(data):
    with open('{}.csv'.format(argv[1]), mode='w') as _file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
        writer = csv.DictWriter(_file, fieldnames=fieldnames)
        e_id = data.get('employee').get('id')
        e_username = data.get('employee').get('username')
        for d in data.get('tasks'):
            writer.writerow({
                "USER_ID": e_id,
                "USERNAME": e_username,
                "TASK_COMPLETED_STATUS": d.get('completed'),
                "TASK_TITLE": d.get('title')
                })


if __name__ == '__main__':
    data = get_employee_tasks(argv[1])
    export_to_csv(data)
