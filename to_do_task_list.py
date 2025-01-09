# Simple To-Do List Manager
def display_menu():
    print("\nTo-Do List Manager")
    print("===================")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Completed")
    print("5. Exit")
    print("===================")


def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for i, (task, completed) in enumerate(tasks, start=1):
            status = "✓" if completed else "✗"
            print(f"{i}. {task} [{status}]")


def add_task(tasks):
    task = input("\nEnter the task: ")
    tasks.append((task, False))
    print(f"Task '{task}' added!")


def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to remove: "))
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task[0]}' removed!")
    except (ValueError, IndexError):
        print("Invalid task number. Please try again.")


def mark_completed(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to mark as completed: "))
        task, _ = tasks[task_num - 1]
        tasks[task_num - 1] = (task, True)
        print(f"Task '{task}' marked as completed!")
    except (ValueError, IndexError):
        print("Invalid task number. Please try again.")


def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            mark_completed(tasks)
        elif choice == '5':
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

