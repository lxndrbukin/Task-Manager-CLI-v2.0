import json
from task import Task

def load_tasks(filepath):
    try:
        with open(filepath, "r") as json_file:
            tasks = json.load(json_file)
            return [task.to_dict() for task in tasks]
    except FileNotFoundError:
        print(f"File at {filepath} not found")
        return []

def save_tasks(filepath, tasks):
    with open(filepath, "w") as json_file:
        data = [Task.to_dict(task) for task in tasks]
        json.dump(data, json_file, indent=4, ensure_ascii=False)