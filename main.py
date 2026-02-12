from task_manager import TaskManager
from task import Status, Priority
from tabulate import tabulate

def display_menu():
    print("\n=== TASK MANAGER ===")
    print("1. Add task")
    print("2. View all tasks")
    print("3. Delete task")
    print("4. Mark complete")
    print("5. Filter by status")
    print("6. Search")
    print("7. Statistics")
    print("0. Exit")


def main():
    manager = TaskManager("tasks.json")

    while True:
        display_menu()
        choice = input("\nEnter choice: ")

        if choice == "1":
            title = input("Please enter the title:\n")
            desc = input("Please enter any additional information/description:\n")
            while True:
                priority = input(f"Please enter the priority for this task ({[p.value for p in Priority]}):\n")
                if priority.lower() not in [p.value for p in Priority]:
                    print("Please enter a valid priority")
                else:
                    break
            while True:
                status = input(f"Please enter the status ({[s.value for s in Status]}):\n")
                if status.lower() not in [s.value for s in Status]:
                    print("Please enter a valid status")
                else:
                    break
            manager.add_task(title=title, desc=desc, priority=priority, status=status)
            print("New task created")
        elif choice == "2":
            tasks = manager.view_all()
            data = [[task.id, task.title, task.desc, task.priority, task.status] for task in tasks]
            print(tabulate(data, headers=["ID", "Title", "Description", "Priority", "Status"]))
        elif choice == "3":
            task_id = input("Please enter the ID of the task you wish to delete:\n")
            deleted = manager.delete_task(task_id)
            if deleted:
                print(f"Task with ID {task_id} has been deleted")
            else:
                print(f"Task with ID {task_id} was not found")
        elif choice == "0":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()