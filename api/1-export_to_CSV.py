#!/usr/bin/python3
"""API PROJECT"""

import requests
import sys
import csv


def get_employee_task_progress(user_id):
    """
    Prints an employee's task progress and exports data to a CSV file.
    """

    user = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos = f"https://jsonplaceholder.typicode.com/todos/?userId={user_id}"

    name = requests.get(user).json().get('name')
    todo = requests.get(todos).json()

    csv_data = [["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]]
    for task in todo:
        csv_data.append([user_id, name, task.get('completed'),
                         task.get('title')])

    csv_file = f"{user_id}.csv"

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        get_employee_task_progress(sys.argv[1])
