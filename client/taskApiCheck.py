import requests


url = "http://localhost:5000/tasks"


def get_tasks():
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return f"Error: {response.status_code}"


def get_task_by_id(task_id):
    response = requests.get(f"{url}/{task_id}")
    if response.status_code == 200:
        return response.json()
    if response.status_code == 404:
        return response.json()["error"]
    return f"Error: {response.status_code}"


def add_task(data):
    response = requests.post(url, json=data)
    if response.status_code == 201:
        return f"success!! to enter {response.json()}"
    return f"Error: {response.status_code}"


def mark_task_complete(task_id):
    response = requests.put(f"{url}/{task_id}")
    if response.status_code == 200:
        return response.json()
    if response.status_code == 404:
        return response.json()["error"]
    return f"Error: {response.status_code}"


def delete_task(task_id):
    response = requests.delete(f"{url}/{task_id}")
    if response.status_code == 200:
        return response.json()
    if response.status_code == 404:
        return response.json()["error"]
    return f"Error: {response.status_code}"
