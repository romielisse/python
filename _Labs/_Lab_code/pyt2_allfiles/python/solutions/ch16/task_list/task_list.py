import db
from objects import Task, TaskList

def display_task_list_names():
    names = db.get_task_list_names()
    print("TASK LISTS")

    for i, name in enumerate(names, start=1):
        print(f"{i}. {name}")
    print()

def get_int(prompt, maxNum):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Invalid whole number. Please try again.\n")
            continue

        if number < 1 or number > maxNum:
            print("That number isn't in the list. Please try again.\n")
        else:
            return number

def select_task_list():
    names = db.get_task_list_names()
    num = get_int("Enter number to select task list: ", len(names))
    name = names[num-1]
    tasks = db.get_task_list(name)
    print(f"{name} task list was selected.\n")
    return name, tasks  # return tuple

def list_tasks(tasks):
    if tasks.count == 0:
        print("There are no tasks in this list.\n")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

def add_task(tasks):
    description = input("Description: ")
    task = Task(description)
    tasks.addTask(task)
    print()

def delete_task(tasks):
    number = get_int("Number: ", tasks.count)
    task = tasks.getTask(number)
    tasks.removeTask(task)
    print()
        
def complete_task(tasks):
    number = get_int("Number: ", tasks.count)   
    task = tasks.getTask(number)
    task.completed = True
    print()
        
def display_menu():
    print("The Task List program")
    print()
    print("COMMAND MENU")
    print("list     - List all tasks")
    print("add      - Add a task")
    print("complete - Complete a task")
    print("delete   - Delete a task")
    print("switch   - Switch selected task list")
    print("exit     - Exit program")
    print()

def main():
    display_menu()
    display_task_list_names()

    name, tasks = select_task_list()
    
    while True:        
        command = input("Command: ")
        if command.lower() == "list":
            list_tasks(tasks)     
        elif command.lower() == "add":
            add_task(tasks)
        elif command.lower() == "delete":
            delete_task(tasks)       
        elif command.lower() == "complete":
            complete_task(tasks)    
        elif command.lower() == "switch":
            db.write_task_list(name, tasks)  # save changes
            name, tasks = select_task_list()
        elif command.lower() == "exit":
            db.write_task_list(name, tasks)  # save changes
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.\n")

if __name__ == "__main__":
    main()
