import sqlite3
from contextlib import closing

from objects import Task

conn = None

def connect():
    global conn
    if not conn:
        DB_FILE = "task_list_db.sqlite"
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row

def close():
    if conn:
        conn.close()

def get_tasks(completed=0):
    query = '''SELECT taskID, description, completed
               FROM Task WHERE completed = ?
               ORDER BY taskID'''
    with closing(conn.cursor()) as c:
        c.execute(query, (completed,))
        results = c.fetchall()

    tasks = []
    for row in results:
        task = Task(row["description"], row["completed"], row["taskID"])
        tasks.append(task)
    return tasks

def add_task(task):
    sql = '''INSERT INTO Task (description, completed) 
             VALUES (?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (task.description, task.completed))
        conn.commit()

def complete_task(task):
    sql = '''UPDATE Task
             SET completed = 1
             WHERE taskID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (task.id,))
        conn.commit()

def delete_task(task):
    sql = '''DELETE FROM task
             WHERE taskID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (task.id,))
        conn.commit()

def main():
    connect()
    print("COMPLETED TASKS")
    tasks = get_tasks(1)
    for task in tasks:
        print(task.id, task.description, task.completed)
        
    print("OPEN TASKS")
    tasks = get_tasks()
    for task in tasks:
        print(task.id, task.description, task.completed)
        
    task = Task("Debug program", False, 5)
    add_task(task)
    complete_task(task)
    print("COMPLETED TASKS")
    tasks = get_tasks(1)
    for task in tasks:
        print(task.id, task.description, task.completed)
        
    delete_task(task)
    print("COMPLETED TASKS")
    tasks = get_tasks(1)
    for task in tasks:
        print(task.id, task.description, task.completed)
    

if __name__ == "__main__":
    main()
