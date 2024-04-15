#!/usr/bin/python3
"""API PROJECT"""

import requests
import sys


def get_employee_task_progress(user_id):
    """
    Prints an employee's task progress.
    """

    user = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos = f"https://jsonplaceholder.typicode.com/todos/?userId={user_id}"

    name = requests.get(user).json().get('name')
    todo = requests.get(todos).json()

    completed_tasks = [task.get('title') for task in todo if
                       task.get('completed')]

    print(f'Employee {name} is done with \
          tasks({len(completed_tasks)}/{len(todo)}):')

    print('\n'.join('\t {}'.format(task) for task in completed_tasks))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        get_employee_task_progress(sys.argv[1])
