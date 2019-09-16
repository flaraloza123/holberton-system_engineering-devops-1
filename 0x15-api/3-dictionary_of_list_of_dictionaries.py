#!/usr/bin/python3
#!/usr/bin/python3

'''
Script for exporting employee data into json
'''

import json
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


def employee_tasks_to_arr(data):
    '''Exports dict to json'''
    _array = []
    for task in data.get('tasks'):
        new_dict = {}
        new_dict['task'] = task.get('title')
        new_dict['completed'] = task.get('completed')
        new_dict['username'] = data.get('employee').get('username')
        _array.append(new_dict)
    return _array


def all_to_dict():
    ''' Converts all employees to dict'''
    res_dict = {}
    for i in range(1, 11):
        print('writing {}'.format(i))
        data = get_employee_tasks(str(i))
        _dict = employee_tasks_to_arr(data)
        res_dict[str(i)] = _dict
        print('complete!')
    return res_dict


if __name__ == '__main__':
    _dict = all_to_dict()
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(_dict, json_file)
