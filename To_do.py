import os

TODO_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task(task):
    tasks = load_tasks()
    tasks.append("[ ] " + task)
    save_tasks(tasks)
    print("✅ Task added.")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def mark_done(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        if tasks[index-1].startswith("[ ]"):
            tasks[index-1] = tasks[index-1].replace("[ ]", "[x]", 1)
            save_tasks(tasks)
            print("✅ Task marked as done.")
        else:
            print("⚠️ Task already done.")
    else:
        print("❌ Invalid task number.")

def remove_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed = tasks.pop(index-1)
        save_tasks(tasks)
        print(f"🗑️ Removed: {removed}")
    else:
        print("❌ Invalid task number.")

def main():
    while True:
        print("\n📋 TO-DO LIST")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Remove task")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            task = input("Enter task: ")
            add_task(task)
        elif choice == '3':
            view_tasks()
            index = int(input("Enter task number to mark as done: "))
            mark_done(index)
        elif choice == '4':
            view_tasks()
            index = int(input("Enter task number to remove: "))
            remove_task(index)
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
