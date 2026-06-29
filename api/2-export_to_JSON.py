#!/usr/bin/python3
"""Export one employee TODO list to JSON."""

import json
import sys
import urllib.request


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"

    user_url = "{}/users/{}".format(url, user_id)
    todo_url = "{}/todos?userId={}".format(url, user_id)

    with urllib.request.urlopen(user_url) as response:
        user = json.loads(response.read().decode("utf-8"))

    with urllib.request.urlopen(todo_url) as response:
        tasks = json.loads(response.read().decode("utf-8"))

    username = user.get("username")
    employee_tasks = []

    for task in tasks:
        employee_tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    with open("{}.json".format(user_id), "w") as json_file:
        json.dump({user_id: employee_tasks}, json_file)
