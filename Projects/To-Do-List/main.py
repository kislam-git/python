import os

tasks = []  # List to store tasks
FILENAME = "tasks.txt"  # File to save tasks

def load_tasks():
    """Load tasks from a file if it exists."""
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            global tasks
            tasks = [line.strip() for line in file.readlines()]

def save_tasks():
    """Save tasks to a file."""
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task():
    """Add a new task to the list."""
    task = input("Enter the task: ")
    tasks.append(task)
    save_tasks()
    print("Task added successfully!")

def remove_task():
    """Remove a task by index."""
    view_tasks()
    try:
        index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            save_tasks()
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def view_tasks():
    """Display all tasks."""
    if not tasks:
        print("No tasks found.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    """Main program loop."""
    load_tasks()
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
