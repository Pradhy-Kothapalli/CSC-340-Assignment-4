import json

TASK_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def create_task():
    task_name = input("Enter task name: ")
    task = {"name": task_name}
    return task

def Read_tasks(tasks):
    if tasks:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['name']}")
    else:
        print("No tasks found.")

def update_task(tasks):
    Read_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter the task number to update: ")) - 1
            new_name = input("Enter the new task name: ")
            tasks[index]["name"] = new_name
            save_tasks(tasks)
            print("Task updated successfully.")
        except (ValueError, IndexError):
            print("Invalid task number.")
    else:
        print("No tasks found.")

def delete_task(tasks):
    Read_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter the task number to delete: ")) - 1
            del tasks[index]
            save_tasks(tasks)
            print("Task deleted successfully.")
        except (ValueError, IndexError):
            print("Invalid task number.")
    else:
        print("No tasks found.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTask Manager")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            tasks.append(create_task())
            save_tasks(tasks)
        elif choice == "2":
            Read_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
