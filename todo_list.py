# CodSoft Internship - Task 1: To-Do List Application
# Author: Nidarshana

tasks = []

def show_menu():
    print("\n=== TO-DO LIST MENU ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Done")
    print("6. Exit")

def add_task():
    task = input("Enter new task: ")
    tasks.append({"task": task, "done": False})
    print(f"✅ Task '{task}' added successfully!")

def view_tasks():
    if not tasks:
        print("📝 No tasks yet. Add some tasks!")
        return
    
    print("\n=== YOUR TO-DO LIST ===")
    for i, item in enumerate(tasks, 1):
        status = "✓ Done" if item["done"] else "⏳ Pending"
        print(f"{i}. {item['task']} - {status}")

def update_task():
    view_tasks()
    if not tasks:
        return
    
    try:
        num = int(input("Enter task number to update: ")) - 1
        if 0 <= num < len(tasks):
            new_task = input("Enter updated task: ")
            tasks[num]["task"] = new_task
            print("✅ Task updated successfully!")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number!")

def delete_task():
    view_tasks()
    if not tasks:
        return
    
    try:
        num = int(input("Enter task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            deleted = tasks.pop(num)
            print(f"🗑️ Task '{deleted['task']}' deleted!")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number!")

def mark_done():
    view_tasks()
    if not tasks:
        return
    
    try:
        num = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["done"] = True
            print(f"🎉 Task '{tasks[num]['task']}' marked as done!")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number!")

def main():
    print("Welcome to To-Do List App by Nidarshana 📝")
    
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            mark_done()
        elif choice == "6":
            print("Thanks for using To-Do List App! Goodbye 👋")
            break
        else:
            print("❌ Invalid choice! Please enter 1-6")

if __name__ == "__main__":
    main()
