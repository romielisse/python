from dataclasses import dataclass

@dataclass
class Category:
    id:int = 0
    name:str = ""
        
@dataclass
class Movie:
    id:int = 0
    name:str = ""
    year:int = 0
    minutes:int = 0
    category:Category = None

