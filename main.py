tasks = []


def load_tasks():
    try:
        with open("tasks.txt", "r", encoding="utf-8") as file:
            loaded_tasks = []
            for line in file.read().splitlines():
                if not line.strip():
                    continue
                if "|" in line:
                    title, status = line.split("|", 1)
                    loaded_tasks.append({"title": title.strip(), "completed": status.strip().lower() == "done"})
                else:
                    loaded_tasks.append({"title": line.strip(), "completed": False})
            return loaded_tasks
    except FileNotFoundError:
        return []


def save_tasks():
    with open("tasks.txt", "w", encoding="utf-8") as file:
        for task in tasks:
            status = "done" if task["completed"] else "pending"
            file.write(f"{task['title']}|{status}\n")


def show_menu():
    print("\n=== To-Do List ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as complete")
    print("4. Edit task")
    print("5. Delete task")
    print("6. Exit")


def add_task():
    task_title = input("Enter task: ").strip()
    if not task_title:
        print("Task cannot be empty.")
        return

    tasks.append({"title": task_title, "completed": False})
    save_tasks()
    print("Task added successfully!")


def view_tasks():
    if not tasks:
        print("No tasks yet.")
        return

    print("Your tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{i}. {status} {task['title']}")


def mark_task_complete():
    if not tasks:
        print("No tasks to mark complete.")
        return

    view_tasks()
    try:
        task_number = int(input("Enter task number to mark complete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        save_tasks()
        print("Task marked as complete!")
    else:
        print("Invalid task number.")


def edit_task():
    if not tasks:
        print("No tasks to edit.")
        return

    view_tasks()
    try:
        task_number = int(input("Enter task number to edit: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if 1 <= task_number <= len(tasks):
        new_title = input("Enter new task name: ").strip()
        if not new_title:
            print("Task cannot be empty.")
            return

        tasks[task_number - 1]["title"] = new_title
        save_tasks()
        print("Task updated successfully!")
    else:
        print("Invalid task number.")


def delete_task():
    if not tasks:
        print("No tasks to delete.")
        return

    view_tasks()
    try:
        task_number = int(input("Enter task number to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if 1 <= task_number <= len(tasks):
        del tasks[task_number - 1]
        save_tasks()
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")


def main():
    global tasks
    tasks = load_tasks()

    while True:
        try:
            show_menu()
            choice = input("Choose an option: ")
        except EOFError:
            print("\nInput closed. Exiting the to-do list.")
            break

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_complete()
        elif choice == "4":
            edit_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

    