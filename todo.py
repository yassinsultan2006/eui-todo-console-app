# To-Do List App (Console Version)
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

   
#task 5: delete a single task 
def delete_task():
    choice = int(input("Enter task number to delete: "))

    if 0 <= choice < len(task_title):
        del task_title[choice]
        del description[choice]
        del priority_level[choice]
        del statuses[choice]
        print("Task deleted successfully")
    else:
        print("Invalid task number")

#clear all completed tasks
def clear_completed_tasks():
    i = 0
    while i < len(statuses):
        if statuses[i].lower() == "completed":
            del task_title[i]
            del description[i]
            del priority_level[i]
            del statuses[i]
        else:
            i += 1
    print("Completed tasks have been cleared")


#task 6
def show_summary():
    total = len(task_title)
    completed = 0
    pending = 0
    
    for s in statuses:
        if s.lower() == "completed":
            completed += 1
        else:
            pending += 1
            
    print("\n--- Task Summary ---")
    print(f"Total Tasks: {total}")
    print(f"Completed: {completed}")
    print(f"Pending: {pending}")


#task 7 
file_name = "tasklist.txt"

def save_tasks():
    # 'w' mode opens the file for writing (overwrites previous data)
    file = open(file_name, "w")
    for i in range(len(task_title)):
        # Grabs the same index from all four parallel lists
        line = f"{task_title[i]},{description[i]},{priority_level[i]},{statuses[i]}\n"
        file.write(line)
    file.close()
    print("Tasks saved successfully")

def load_tasks():
    # Create the file if it doesn't exist so it doesn't crash on the first run
    open(file_name, "a").close() 
    file = open(file_name, "r")
    for line in file:
        data = line.strip().split(",") 
        if len(data) == 4:
            task_title.append(data[0])
            description.append(data[1])
            priority_level.append(data[2])
            statuses.append(data[3])
    file.close()
    print("Tasks have been loaded")


load_tasks()
task_status()
filter_tasks()
show_summary() 
edit_task()     
delete_task()
clear_completed_tasks()
save_tasks()