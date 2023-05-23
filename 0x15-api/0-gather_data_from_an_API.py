#!/usr/bin/python3
"""python module that retuns employee information"""
import urllib
import request
import json

def get_employee_todo_progress(employee_id):
    """function that returns employee id"""
    base_url = 'https://jsonplaceholder.typicode.com/'
    employee_url = '{}/employees/{}'.format(base_url, employee_id)
    todos_url = '{}/todos?employeeId={}'.format(base_url, employee_id)

    
    try:
        with urllib.request.urlopen(employee_url) as response:
            employee_data = json.loads(response.read().decode())
            employee_name = employee_data.get('name')
    except urllib.error.HTTPError as e:
        print("Error: Failed to retrieve employee data (status code: {})".format(e.code))
        return

    
    try:
        with urllib.request.urlopen(todos_url) as response:
            todos_data = json.loads(response.read().decode())
            total_tasks = len(todos_data)
            completed_tasks = [todo for todo in todos_data if todo.get('completed')]
            num_completed_tasks = len(completed_tasks)
    except urllib.error.HTTPError as e:
        print("Error: Failed to retrieve TODO list (status code: {})".format(e.code))
        return

    
    print("Employee {} is done with tasks ({}/{}):".format(employee_name, num_completed_tasks, total_tasks))
    print("{}: {} completed tasks out of {}".format(employee_name, num_completed_tasks, total_tasks))

    
    for task in completed_tasks:
        task_title = task.get('title')
        print("\t{}".format(task_title))


if __name__ == "__main__:
