#!/usr/bin/python3
""""Python script that returns information about his/her TODO list progress
"""
import urllib.request
import json


def get_employee_todo(employee_id):
    """return employees to do list progress"""
    base_url = 'https://jsonplaceholder.typicode.com/'
    employee_url = '{}/employees/{}'.format(base_url, employee_id)
    todos_url = '{}/todos?employeeId={}'.format(base_url, employee_id)

    try:
        with urllib.request.urlopen(employee_url) as response:
            employee_data = json.loads(response.read().decode())
            employee_name = employee_data.get('name')
    except urllib.error.HTTPError as e:
        print("Error: failed to retrive employee data(status code: {})".format(
            e.code))
        return

    try:
        with urllib.request.urlopen(todos_url) as reponse:
            todos_data = json.loads(response.read().decode())
            total_task = len(todos_data)
            complete = [todo for todo in todos_data if todo.get('completed')]
            number_complete = len(complete)
    except urllib.request.HTTPError as e:
        print("Error: Failed to retrive TODO list (status code: {})".format(
            e.code))
        return

    print("Employee {} is done with tasks ({}/{}:".format(
        employee_name, number_complete, total_task))
    print("{}: {} completed tasks out of {}".format(
        employee_name, number_complete, total_task))
    for task in complete:
        task_title = task.get('title')
        print("\t{}".format(task_title))


if __name__ == "__main__":
