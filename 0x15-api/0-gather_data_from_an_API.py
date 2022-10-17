#!/usr/bin/python3
"""
Gather data from an API
"""
import requests
from sys import argv


if __name__ == "__main__":

    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users/"
    id = argv[1]

    name = requests.get(users_url + id).json()
    task = requests.get(todos_url, params={"userId": id}).json()
    total_task = requests.get(
        todos_url, params={"completed": "true", "userId": id}).json()

    print("Employee {} is done with tasks({}/{}):"
          .format(name.get("name"), len(total_task), len(task)))

    for task in total_task:
        print("\t {}".format(task.get("title")))
