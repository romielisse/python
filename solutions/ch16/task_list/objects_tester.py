from objects import Task, TaskList

task1 = Task("Pay bills")
task2 = Task("Get groceries")
task3 = Task("Make dentist appointment")

tasks = TaskList("Personal")
tasks.addTask(task1)
tasks.addTask(task2)
tasks.addTask(task3)

task = tasks.getTask(1)
task.completed = True

print(tasks)

tasks.removeTask(task)

print(tasks)
