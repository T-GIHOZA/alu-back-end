#!/usr/bin/python3
"""Export all employees TODO lists to JSON."""

import json
import urllib.request


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"

    with urllib.request.urlopen("{}/users".format(url)) as response:
        users = json.loads(response.read().decode("utf-8"))

    with urllib.request.urlopen("{}/todos".format(url)) as response:
        tasks = json.loads(response.read().decode("utf-8"))

    all_tasks = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        all_tasks[str(user_id)] = []

        for task in tasks:
            if task.get("userId") == user_id:
                all_tasks[str(user_id)].append({
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)
