def show_menu():
    print("Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")


def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed":False})
    print("Task added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")

    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Not completed"
            print(f"{i}. {task['task']} - {status}")

def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as completed: ")) - 1
        tasks[task_number]["completed"] = True
        print("Task marked as completed!")
    except (ValueError, IndexError):
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to delete: ")) - 1
        del tasks[task_number]
        print("Task deleted!")
    except (ValueError, IndexError):
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting the To-Do List app.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
