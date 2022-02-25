from dataclasses import dataclass

@dataclass
class Task:
    description:str = ""
    completed:bool = False   # can also use type hint of int 
    id:int = 0

    def __str__(self):
        completed_str = ""
        if self.completed == True:
            completed_str = " (DONE!)"            
        return self.description + completed_str

def main():
    task1 = Task("Fix bike", True, 1)
    print(task1)    
    task2 = Task("Call mom", False, 2)
    print(task2)

if __name__ == "__main__":
    main()
