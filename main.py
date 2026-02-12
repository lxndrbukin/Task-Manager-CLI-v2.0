from task_manager import TaskManager
from task import Status, Priority
from utils import get_enum_value, print_tasks_table
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
            priority = get_enum_value("Please enter the priority", Priority)
            status = get_enum_value("Please enter the status", Status)
            manager.add_task(title=title, desc=desc, priority=priority, status=status)
            print("New task created")
        elif choice == "2":
            tasks = manager.view_all()
            print_tasks_table(tasks)
        elif choice == "3":
            task_id = input("Please enter the ID of the task you wish to delete:\n")
            deleted = manager.delete_task(task_id)
            if deleted:
                print(f"Task with ID {task_id} has been deleted")
            else:
                print(f"Task with ID {task_id} was not found")
        elif choice == "4":
            task_id = input("Please enter the ID of the task you wish to mark as completed:\n")
            completed = manager.mark_complete(task_id)
            if completed:
                print(f"Task with ID {task_id} has been completed")
            else:
                print(f"Task with ID {task_id} was not found")
        elif choice == "5":
            status = input("Please enter the status:\n")
            tasks = manager.filter_by_status(status)
            print_tasks_table(tasks)
        elif choice == "6":
            keyword = input("Please enter the search term:\n")
            tasks = manager.search(keyword)
            print_tasks_table(tasks)
        elif choice == "0":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()