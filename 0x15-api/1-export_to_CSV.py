#!/usr/bin/python3
"""This script retrieves task data for a given user 
from a public API and exports the data in CSV format.
"""
import csv
import requests
import sys


def main():
    """A script that returns employee id"""
    if len(sys.argv) < 2:
        print("Please provide the user ID as an argument.")
        return

    user_id = sys.argv[1]
    main_url = 'https://jsonplaceholder.typicode.com'

    try:
        todo_url = f"{main_url}/users/{user_id}/todos"
        name_url = f"{main_url}/users/{user_id}"

        todo_response = requests.get(todo_url)
        name_response = requests.get(name_url)

        todo_result = todo_response.json()
        name_result = name_response.json()

        name = name_result.get("name")

        filename = f"{user_id}.csv"
        with open(filename, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            for todo in todo_result:
                task_completed_status = "Completed" if todo["completed"] else "Not Completed"
                task_title = todo["title"]
                writer.writerow([user_id, name, task_completed_status, task_title])

        print(f"Task data exported to {filename} successfully.")

    except requests.exceptions.RequestException as e:
        print("An error occurred: {}".format(e))


if __name__ == '__main__':
    main()

