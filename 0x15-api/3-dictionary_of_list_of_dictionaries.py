#!/usr/bin/python3
"""
Exports todo list information for all employees ID
in the JSON format as dictionary
"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    all_users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({u.get("id"): [{
            "task": t["title"],
            "completed": t["completed"],
            "username": u["username"]
            } for t in requests.get(url + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in all_users}, jsonfile)
