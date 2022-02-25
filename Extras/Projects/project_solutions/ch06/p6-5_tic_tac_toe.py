#!/usr/bin/env python3

grid = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]


def main():
    print("Welcome to Tic Tac Toe")
    display_grid()
    start_game()


def start_game():
    game_over = False
    while not game_over:
        game_over = take_turn()
    print()
    print("Game over!")


def take_turn():
    turn = 1
    while True:
        if not turn % 2 == 0:
            mark = "X"
        else:
            mark = "O"
        print(f"{mark}'s turn")

        row = int(input("Pick a row (1, 2, 3): "))
        if row < 1 or row > 3:
            print("Invalid row number. Try again.")
            continue

        column = int(input("Pick a column (1, 2, 3): "))
        if column < 1 or column > 3:
            print("Invalid column number. Try again.")
            continue

        if not grid[row-1][column-1] == " ":
            print("This square is already taken. Try again.")
            continue

        grid[row-1][column-1] = mark
        display_grid()

        winner = check_for_winner()
        if winner == "X" or winner == "O":
            print(f"{winner} wins!")
            game_over = True
            return game_over

        if turn == 9:
            print("It's a tie!")
            game_over = True
            return game_over

        turn += 1


def display_grid():
    print()
    print("+---+---+---+")
    for row in grid:
        print("|", end="")
        for column in row:
            print(f" {column} |", end="")
        print()
        print("+---+---+---+")
    print()


def check_for_winner():
    # rows
    for x in range(3):
        if grid[x][0] == grid[x][1] and grid[x][1] == grid[x][2]:
            return grid[x][0]

    # columns
    for y in range(3):
        if grid[0][y] == grid[1][y] and grid[1][y] == grid[2][y]:
            return grid[0][y]

    # diagonal 1
    if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]:
        return grid[0][0]

    # diagonal 2
    if grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0]:
        return grid[2][0]

    # no winner yet
    return " "

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
