#!/usr/bin/env python3

# display a welcome message
print("The Test Scores application")
print()
print("Enter test scores")
print("Enter 999 to end input")
print("======================")

# initialize variables
counter = 0
score_total = 0
test_score = 0
user_continue = "y"

while(user_continue.lower() == "y"):

    counter = 0
    score_total = 0
    test_score = 0
    print()

    while test_score != 999:
        # get test score
        test_score = int(input("Enter test score: "))
    
        if test_score >= 0 and test_score <= 100:
            score_total += test_score
            counter += 1
        elif test_score == 999:
            break
        else:
            print(f"Test score must be from 0 through 100. "
                f"Score discarded. Try again.")

    # calculate average score
    average_score = round(score_total / counter)
                    
    # format and display the result
    print("======================")
    print(f"Total Score: {score_total}"
        f"\nAverage Score: {average_score}")
        
    user_continue = input("\nEnter another set of test scores (y/n)? ")

print()
print("Bye!")


