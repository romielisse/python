FILENAME = "preferences.txt"

def read_preferences():    
    preferences = {}
    with open(FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            line = line.split("|")
            key = line[0]
            value = line[1]
            preferences[key] = value
    return preferences

def write_preferences(preferences):
    with open(FILENAME, "w") as file:
        for key, value in preferences.items():
            file.write(key + "|" + str(value) + "\n")

def main():
    preferences = {"name": "Joel Murach",
                   "language": "English",
                   "autosave": 10}

    write_preferences(preferences)

    preferences = read_preferences()
    for key, value in preferences.items():
        print(key + ":" + value)


if __name__ == "__main__":
    main()
