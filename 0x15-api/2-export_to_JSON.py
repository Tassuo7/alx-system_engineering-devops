#!/usr/bin/python3
"""
Exports todo list information for a given employee ID in the JSON format
"""
import json
import requests
import sys

if __name__ == "__main__":
    uid = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    userId = requests.get(url + "users/{}".format(uid)).json()
    todos = requests.get(url + "todos", params={"userId": uid}).json()
    un = userId.get("username")

    with open("{}.json".format(uid), "w") as jsonfile:
        for t in todos:
            json_file = [{
                "task": t["title"], "completed": t["completed"], "username": un
                }]
            json.dump({uid: json_file}, jsonfile)
