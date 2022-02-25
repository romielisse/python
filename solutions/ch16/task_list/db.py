import csv
from objects import Task, TaskList

def get_task_list_names():
    task_lists = []
    with open("task_lists.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            task_lists.append(line)
    return task_lists

def write_task_list(name, tasks):
    # convert the TaskList object to a list of lists
    rows = []
    for task in tasks:
        row = []
        row.append(task.description)
        row.append(task.completed)
        rows.append(row)

    # write list of lists to CSV file
    filename = "task_list_" + name.lower() + ".csv"    
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def get_task_list(name):
    filename = "task_list_" + name.lower() + ".csv"
    tasks = TaskList(name)
    with open(filename, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            # convert row to Task object
            task = Task(row[0])
            if row[1] == 'True':
                task.completed = True
            tasks.addTask(task)
    return tasks

def main():
    task_list_names = get_task_list_names()
    name = task_list_names[0]
    tasks = TaskList(name)
    
    task1 = Task("Buy toothbrush")
    tasks.addTask(task1)
    task2 = Task("Do homework")
    task2.completed = True
    tasks.addTask(task2)
    write_task_list(name, tasks)

    tasks = get_task_list(name)
    print(tasks)
    
    
if __name__ == "__main__":
    main()
