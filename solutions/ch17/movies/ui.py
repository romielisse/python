#!/usr/bin/env/python3

import db
from objects import Movie

def display_title():
    print("The Movie List program")
    print()    
    display_menu()

def display_menu():
    print("COMMAND MENU")
    print("cat  - View movies by category")
    print("year - View movies by year")
    print("min  - View movies by minutes")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("exit - Exit program")
    print()    

def display_categories():
    print("CATEGORIES")
    categories = db.get_categories()    
    for category in categories:
        print(f"{category.id}. {category.name}")
    print()

def display_movies(movies, title_term):
    print(f"MOVIES - {title_term}")

    print(f"{'ID':3s} {'Name':37s} {'Year':6s} {'Mins':5s} {'Category':10s}")
    print("-" * 64)
    for movie in movies:
        print(f"{movie.id:<3d} {movie.name:37s} {movie.year:<6d}",
              f"{movie.minutes:<5d} {movie.category.name:10s}")                               
    print()

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid whole number. Please try again.\n")

def display_movies_by_category():
    category_id = get_int("Category ID: ")
    category = db.get_category(category_id)
        
    if category == None:
        print("There is no category with that ID.\n")
    else:
        print()
        movies = db.get_movies_by_category(category_id)
        display_movies(movies, category.name.upper())
        
def display_movies_by_year():
    year = get_int("Year: ")
    print()
    movies = db.get_movies_by_year(year)
    display_movies(movies, year)

def display_movies_by_minutes():
    max_minutes = get_int("Maximum number of minutes: ")
    print()
    movies = db.get_movies_by_minutes(max_minutes)
    display_movies(movies, f"LESS THAN {max_minutes} MINUTES")

def add_movie():
    name        = input("Name: ")
    year        = get_int("Year: ")
    minutes     = get_int("Minutes: ")
    category_id = get_int("Category ID: ")

    category = db.get_category(category_id)
    if category == None:
        print("There is no category with that ID. Movie NOT added.\n")
    else:
        movie = Movie(name=name, year=year, minutes=minutes,
                      category=category)
        db.add_movie(movie)
        print(f"{name} was added to database.\n")
    
def delete_movie():
    movie_id = get_int("Movie ID: ")
    movie = db.get_movie(movie_id)

    if movie == None:
        print("There is no movie with that ID. Movie NOT deleted.\n")
    else:
        msg = f"Are you sure you want to delete '{movie.name}'? (y/n): "
        choice = input(msg)
        if choice == "y":
            db.delete_movie(movie_id)
            print(f"'{movie.name}' was deleted from database.\n")
        else:
            print(f"'{movie.name}' was NOT deleted from database.\n")        
        
def main():
    db.connect()
    display_title()
    display_categories()
    
    while True:        
        command = input("Command: ")
        if command == "cat":
            display_movies_by_category()
        elif command == "year":
            display_movies_by_year()
        elif command == "min":
            display_movies_by_minutes()
        elif command == "add":
            add_movie()
        elif command == "del":
            delete_movie()
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
            display_menu()
    db.close()
    print("Bye!")

if __name__ == "__main__":
    main()
