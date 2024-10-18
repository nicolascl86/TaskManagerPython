import os

# File to store tasks
TASK_FILE = 'tasks.txt'

def read_tasks():
    """Read tasks from the file."""
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as file:
            tasks = file.readlines()
        # Strip newline characters
        tasks = [task.strip() for task in tasks]
    else:
        tasks = []
    return tasks

def write_tasks(tasks):
    """Write tasks to the file."""
    with open(TASK_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def main():
    # Read existing tasks
    tasks = read_tasks()
    
    # Prompt user for a new task
    new_task = input("What is the new task? ")
    
    # Add the new task to the list
    tasks.append(new_task)
    
    # Write the updated task list back to the file
    write_tasks(tasks)
    
    print("Task added successfully!")

if __name__ == "__main__":
    main()