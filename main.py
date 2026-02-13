from task_manager import TaskManager
from task import Status, Priority
from utils import get_enum_value, print_tasks_table, print_stats
from config import create_config, save_config, load_config, check_config
from ai.ai_helper import extract_task_from_text

def display_menu():
    print("\n=== TASK MANAGER ===")
    print("1. Add task")
    print("2. View all tasks")
    print("3. Delete task")
    print("4. Mark complete")
    print("5. Filter by status")
    print("6. Filter by priority")
    print("7. Search")
    print("8. Statistics")
    print("9. Settings")
    print("0. Exit")

def settings_menu():
    print("\n=== TASK MANAGER SETTINGS ===")
    print("1. Update storage path")
    print("2. Enable/Update AI")
    print("0. Exit settings")


def main():
    if not check_config():
        save_config(create_config())
    config = load_config()
    manager = TaskManager(config["main"]["storage"])
    while True:
        display_menu()
        choice = input("\nEnter choice: ")
        if choice == "1":
            if config["ai"]["enabled"]:
                use_ai = input("Use AI to create task from description? (y/n): ").lower()
                if use_ai == "y":
                    user_input = input("Describe your task in natural language:\n")
                    task_data = extract_task_from_text(user_input, config)

                    if task_data:
                        print(f"\nAI extracted:")
                        print(f"Title: {task_data["title"]}")
                        print(f"Description: {task_data["desc"]}")
                        print(f"Priority: {task_data["priority"]}")
                        print(f"Status: {task_data["status"]}")

                        confirm = input("\nCreate this task? (y/n): ").lower()
                        if confirm == "y":
                            manager.add_task(
                                title=task_data["title"],
                                desc=task_data["desc"],
                                priority=task_data["priority"],
                                status=task_data["status"]
                            )
                            print("Task created with AI!")
                        else:
                            print("Task cancelled")
                    else:
                        print("AI extraction failed. Please try again or use manual entry.")
            else:
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
            try:
                task_id = int(input("Please enter the ID of the task you wish to delete:\n"))
                deleted = manager.delete_task(task_id)
                if deleted:
                    print(f"Task with ID {task_id} has been deleted")
                else:
                    print(f"Task with ID {task_id} was not found")
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif choice == "4":
            try:
                task_id = int(input("Please enter the ID of the task you wish to mark as completed:\n"))
                completed = manager.mark_complete(task_id)
                if completed:
                    print(f"Task with ID {task_id} has been completed")
                else:
                    print(f"Task with ID {task_id} was not found")
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif choice == "5":
            status = get_enum_value("Please enter the status", Status)
            tasks = manager.filter_by_status(status)
            print_tasks_table(tasks)
        elif choice == "6":
            priority = get_enum_value("Please enter the priority", Priority)
            tasks = manager.filter_by_priority(priority)
            print_tasks_table(tasks)
        elif choice == "7":
            keyword = input("Please enter the search term:\n")
            tasks = manager.search(keyword)
            print_tasks_table(tasks)
        elif choice == "8":
            stats = manager.get_stats()
            print_stats(stats)
        elif choice == "9":
            config = load_config()
            settings_menu()
            while True:
                setting_choice = input("\nSelect an option:\n")
                if setting_choice == "1":
                    config["main"]["storage"] = input("Provide new path for task storage:\n")
                    save_config(config)
                    print("\nConfig updated")
                    config = load_config()
                    manager = TaskManager(config["main"]["storage"])
                elif setting_choice == "2":
                    config["ai"]["provider"] = input("Enter the AI model provider (Anthropic, xAI, OpenAI):\n").lower()
                    config["ai"]["model"] = input("Enter the desired AI model (e.g. gpt-3.5-turbo, grok-3-mini, claude-opus-4-6):\n").lower()
                    config["ai"]["api_key"] = input("Enter the API key for your chosen provider:\n")
                    print("\nConfig updated")
                    save_config(config)
                elif setting_choice == "0":
                    break
        elif choice == "0":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()