
# 2. To-Do List App (Console Version)
# A personal task management system for organizing daily activities.
# **Features:**

# - Add tasks with titles, descriptions, and priority levels (low/medium/high)
# - Mark tasks as completed or pending
# - View tasks filtered by status or priority
# - Edit task details after creation

# - Delete tasks individually or clear all completed tasks
# - Show daily or weekly task summary
# - Save tasks automatically so they persist between sessions


# task 1: seting up and adding tasks
task_title = []
description = []
priority_level = [] 
statuses = []

def add_task():
    t = input("Enter task title: ")
    d = input("Enter task description: ")
    p = input("Enter task priority level (low/medium/high): ")
    
    task_title.append(t)
    description.append(d)
    priority_level.append(p)
    statuses.append("Pending") 
    print("Task added Successfully")

# This part runs the "Add Task" loop
cont = "yes"
while cont.lower() == "yes":
    add_task()
    cont = input("Do you want to add another task? (yes/no): ").lower()

print("\nFinished Adding Tasks")

# task 2: marking task status
def task_status():
    for i in range(len(task_title)):
        print(f"Number {i}: {task_title[i]}, {description[i]}, {priority_level[i]}, {statuses[i]}")

    while True:
        choice = int(input("\nEnter the number of the task you want to update: "))

        if 0 <= choice < len(task_title):
            new_status = input("Enter new status (pending/completed): ").lower()

            if new_status == "completed" or new_status == "pending":
                statuses[choice] = new_status
                print(f"Task marked as {new_status}.")
                break
            else:
                print("Invalid status. Please enter 'pending' or 'completed'.")
        else:
            print("Invalid task number. Please try again.")


# task 3: filtering
def filter_tasks():
    category = input("Enter filter category (status/priority): ").lower()

    if category == "status":
        choice = input("Enter status (pending/completed): ").lower()
        print(f"Showing {choice} tasks")
        for i in range(len(task_title)):
            if statuses[i].lower() == choice:
                print(f" Task is {task_title[i]} and status is {statuses[i]}")

    elif category == "priority":
        choice = input("Enter priority (low/medium/high): ").lower()
        print(f"Showing {choice} priority tasks")
        for i in range(len(task_title)):
            if priority_level[i].lower() == choice:
                print(f" Task is {task_title[i]} and priority is {priority_level[i]}")
    else:
        print("Invalid category")


# task 4: editing task details
def edit_task():
    edit_cont = "yes"
    while edit_cont.lower() == "yes":

        choice = int(input("Enter the task number to edit: "))
    
        if choice >= 0 and choice < len(task_title):
            part = input("Do you want to edit the title or description or priority? ").lower()
            
            if part == "title":
                task_title[choice] = input("Enter new title: ")
            elif part == "description":
                description[choice] = input("Enter new description: ")
            elif part == "priority":
                priority_level[choice] = input("Enter new priority: ")
            else:
                print("Invalid choice.")
            
            print("Update complete!")
            edit_cont = input("Do you want to edit another task? (yes/no): ").lower()
        else:
            print("Invalid task number.")
            edit_cont = input("Invalid number! Try again? (yes/no): ").lower()

   


task_status()
filter_tasks()
edit_task()     
