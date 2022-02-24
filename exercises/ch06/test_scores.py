#!/usr/bin/env python3

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    scores = []
    while True:
        score = input("Enter test score: ")
        if score == "x":
            return scores
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                scores.append(score)
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

    return scores

def process_scores(scores):

    score_total = 0

    # calculate average score
    for score in scores:
        score_total += score

    average = score_total / len(scores)
                
    # format and display the result
    print()
    print("Score total:       ", score_total)
    print("Number of Scores:  ", len(scores))
    print("Average Score:     ", average)

def main():
    display_welcome()
    scores = get_scores()
    process_scores(scores)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


