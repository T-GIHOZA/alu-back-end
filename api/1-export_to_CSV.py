#!/usr/bin/python3
"""Export one employee TODO list to CSV."""

import csv
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

    with open("{}.csv".format(user_id), "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in tasks:
            writer.writerow([
                user_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
