#!/usr/bin/python3
"""API PROJECT"""

import json
import requests
import sys


def get_employee_task_progress(user_id):
    """
    Exports an employee's task progress to a JSON file.
    """

    user = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos = f"https://jsonplaceholder.typicode.com/todos/?userId={user_id}"

    user = requests.get(user).json()
    todo = requests.get(todos).json()

    tasks = []
    for task in todo:
        tasks.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user.get('username')
        })

    data = {user_id: tasks}

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        get_employee_task_progress(sys.argv[1])
