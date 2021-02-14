import requests
import os

body = {
    "summary": "Take out trash",
    "description": ""
}

resp = requests.post(
    url='https://todolist.example.com/tasks/',
    json=body
)

if resp.status_code != 201:
    print(f'POST /tasks/ {resp.status_code}')

print(f'Created task. ID: {resp.json()["id"]}')
