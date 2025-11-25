import json
import os

FILE_NAME = "tasks.json"

# Load existing tasks from the file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to the file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Display all tasks
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks available. Add some!\n")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "✔" if task['done'] else "✘"
        print(f"{i}. {task['task']}  [{status}]")
    print()

# Add a new task
def add_task(tasks):
    task_name = input("Enter task: ")
    tasks.append({"task": task_name, "done": False})
    save_tasks(tasks)
    print("Task added!\n")

# Mark task as done
def mark_done(tasks):
    show_tasks(tasks)
    try:
        choice = int(input("Enter task number to mark as done: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["done"] = True
            save_tasks(tasks)
            print("Task marked as done!\n")
        else:
            print("Invalid choice.\n")
    except ValueError:
        print("Enter a valid number.\n")

# Delete a task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        choice = int(input("Enter task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f"Deleted task: {removed['task']}\n")
        else:
            print("Invalid choice.\n")
    except ValueError:
        print("Enter a valid number.\n")

# Main menu
def main():
    tasks = load_tasks()

    while True:
        print("==== TO-DO LIST ====")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")

if __name__ == "__main__":
    main()
