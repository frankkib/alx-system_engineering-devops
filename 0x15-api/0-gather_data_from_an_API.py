#!/usr/bin/python3
"""python module fo return the number of finshed tasks"""
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
        todo_url = "{}/users/{}/todos".format(main_url, user_id)
        name_url = "{}/users/{}".format(main_url, user_id)

        todo_response = requests.get(todo_url)
        name_response = requests.get(name_url)

        todo_result = todo_response.json()
        name_result = name_response.json()

        todo_num = len(todo_result)
        todo_complete = sum(1 for todo in todo_result if todo["completed"])

        name = name_result.get("name")

        print("Employee {} is done with tasks ({}/{})".format(
            name, todo_complete, todo_num))
        for todo in todo_result:
            if todo["completed"]:
                print("\t{}".format(todo['title']))
    except requests.exceptions.RequestException as e:
        print("An error occurred: {}".format(e))


if __name__ == '__main__':
    main()
