from tabulate import tabulate

def get_enum_value(prompt, enum_class):
    valid_values = [e.value for e in enum_class]
    while True:
        value = input(f"{prompt} ({valid_values}):\n")
        if value.lower() in valid_values:
            return value
        print("Please enter a valid status")

def print_tasks_table(tasks):
    headers = ["ID", "Title", "Description", "Priority", "Status"]
    data = [[task.id, task.title, task.desc, task.priority, task.status] for task in tasks]
    print(tabulate(data, headers))