from dataclasses import dataclass

@dataclass
class Task:
    description:str = ""
    completed:bool = False

    def __str__(self):
        completed_str = ""
        if self.completed == True:
            completed_str = " (DONE!)"            
        return self.description + completed_str
    
@dataclass
class TaskList:
    name:str = ""

    def __post_init__(self): 
        self.__tasks = []

    def addTask(self, task):
        self.__tasks.append(task)

    def getTask(self, number):
        index = number - 1
        return self.__tasks[index]      

    def removeTask(self, task):
        self.__tasks.remove(task)

    @property
    def count(self):
        return len(self.__tasks)    

    def __iter__(self):
        for task in self.__tasks:
            yield task

    def __str__(self):
        tasks_str = ""
        for task in self.__tasks:
            tasks_str += str(task) + " | "
        tasks_str = tasks_str[:-3] # remove final separator 
        return tasks_str
