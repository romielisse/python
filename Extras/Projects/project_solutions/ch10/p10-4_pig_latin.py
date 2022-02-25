#!/usr/bin/env python3

def to_pig_latin(word):
    ch = word[0]
    if (ch == 'a' or
        ch == 'e' or
        ch == 'i' or
        ch == 'o' or
        ch == 'u'):
        word += "way"
    else:
        if ch == 'y':
            word = word[1:]
            word += ch
            ch = word[0]
        while (ch != 'a' and
               ch != 'e' and
               ch != 'i' and
               ch != 'o' and
               ch != 'u' and
               ch != 'y'):
            word = word[1:]
            word += ch
            ch = word[0]
        word += "ay"
    return word

def main():
    print("Pig Latin Translator")
    print()

    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        line = input("Enter text: ").strip()

        # remove punctuation from English
        line = line.replace(".", "")
        line = line.replace(",", "")
        line = line.replace("!", "")
        line = line.replace("?", "")

        # make English lower case
        line = line.lower()

        # translate to Pig Latin and display
        if line == "":
            print("You didn't enter any text.\n")
        else:
            #translate
            words1 = line.split(" ")
            words2 = []
            for word in words1:
                words2.append(to_pig_latin(word))
            pig_latin = " ".join(words2)

            # display         
            print("English:   ", line)
            print("Pig Latin: ", pig_latin)
            print()

        # Continue?
        choice = input("Continue? (y/n): ")
        print()
        
    print("Bye!")        


if __name__ == "__main__":
    main()
