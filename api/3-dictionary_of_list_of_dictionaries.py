#!/usr/bin/python3
"""API PROJECT"""

import requests
import json


def get_all_employees_tasks():
    """
    Exports tasks from all employees to a JSON file.
    """

    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    all_tasks = {}

    for user in users:
        user_id = user.get('id')
        todos = requests.get(
            f"https://jsonplaceholder.typicode.com/todos/?userId={user_id}"
            ).json()

        tasks = []
        for task in todos:
            tasks.append({
                "username": user.get('username'),
                "task": task.get('title'),
                "completed": task.get('completed')
            })

        all_tasks[user_id] = tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)


if __name__ == "__main__":
    get_all_employees_tasks()
