#!/usr/bin/python3
"""Get TODO list progress for one employee."""

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

    done_tasks = []
    for task in tasks:
        if task.get("completed"):
            done_tasks.append(task)

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done_tasks), len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
