import random

import json

 

# Base class for shared Sudoku functionality

class SudokuBase:

    def __init__(self):

        # Initialize the board fields (4x4 Sudoku)

        self.game = [[0 for _ in range(4)] for _ in range(4)]

        self.solution = [[0 for _ in range(4)] for _ in range(4)]

        self.initial_game = [[0 for _ in range(4)] for _ in range(4)]

 

    def print_board(self, board):

        # Print the Sudoku board with borders

        print("+---+---+---+---+")

        for row in board:

            print("| " + " | ".join(str(num) if num != 0 else "_" for num in row) + " |")

            print("+---+---+---+---+")

 

# Extended class for game logic

class SudokuGame(SudokuBase):

    def __init__(self):

        super().__init__()

 

    # Validity check for Solution

    def is_valid_row(self, number, row):

        # Check if a number is valid in the given row

        return number not in self.solution[row]

 

    def is_valid_column(self, number, column):

        # Check if a number is valid in the given column

        for i in range(4):

            if self.solution[i][column] == number:

                return False

        return True

 

    def is_valid_box(self, number, row, col):

        # Check if a number is valid in the 2x2 box

        row_start = (row // 2) * 2

        col_start = (col // 2) * 2

        for i in range(2):

            for j in range(2):

                if self.solution[row_start + i][col_start + j] == number:

                    return False

        return True

 

    def is_valid_move(self, row, column, number):

        # Check if placing a number is valid

        return (self.is_valid_row(number, row) and

                self.is_valid_column(number, column) and

                self.is_valid_box(number, row, column) and

                self.initial_game[row][column] == 0)

 

# Validity check for Moves played

    def is_move_valid_row(self, number, row):

        # Check if a number is valid in the given row

        return number not in self.initial_game[row]

 

    def is_move_valid_column(self, number, column):

        # Check if a number is valid in the given column

        for i in range(4):

            if self.initial_game[i][column] == number:

                return False

        return True

 

    def is_move_valid_box(self, number, row, col):

        # Check if a number is valid in the 2x2 box

        row_start = (row // 2) * 2

        col_start = (col // 2) * 2

        for i in range(2):

            for j in range(2):

                if self.initial_game[row_start + i][col_start + j] == number:

                    return False

        return True

 

    def is_move_valid_move(self, row, column, number):

        # Check if placing a number is valid

        return (self.is_move_valid_row(number, row) and

                self.is_move_valid_column(number, column) and

                self.is_move_valid_box(number, row, column) and

                self.initial_game[row][column] == 0)

 

 

 

    def fill_board(self):

        # Fill the board with a valid Sudoku solution

        def backtrack(cell=0):

            if cell == 16: # All cells are filled

                return True

            row, col = divmod(cell, 4)

 

            numbers = list(range(1, 5))

            random.shuffle(numbers)

            for number in numbers:

                if self.is_valid_move(row, col, number):

                    self.solution[row][col] = number

                    if backtrack(cell + 1):

                        return True

                    self.solution[row][col] = 0

            return False

 

        backtrack()

 

    def build_game(self):

        # Build the Sudoku game solution and puzzle

        self.fill_board()

        for i in range(4):

            for j in range(4):

                self.initial_game[i][j] = self.solution[i][j]

 

        self.mask_cells()

 

    def mask_cells(self):

        # Mask cells to create the playable puzzle

        count = 8 # Number of cells to mask

        while count > 0:

            row = random.randint(0, 3)

            column = random.randint(0, 3)

            if self.initial_game[row][column] != 0:

                self.initial_game[row][column] = 0

                count -= 1

 

    def save_to_file(self, filename):

        # Save the current puzzle to a JSON file

        try:

            data = {

                "solution": self.solution,

                "initial_game": self.initial_game

            }

            with open(filename, "w") as file:

                json.dump(data, file)

        except Exception as e:

            print("Error saving file:", e)

 

    def load_from_file(self, filename):

        # Load a puzzle from a JSON file

        try:

            with open(filename, "r") as file:

                data = json.load(file)

                self.solution = data.get("solution", [])

                self.initial_game = data.get("initial_game", [])

        except FileNotFoundError:

            print("File not found. Make sure the file exists.")

        except Exception as e:

            print("Error loading file:", e)

 

    def play_game(self):

        # Allow the user to interactively solve the puzzle

        print("\nStarting Sudoku Game! /n/nEnter your moves in the format: row column number")

        print("Numbers must be within the grid (0-3 for rows/columns, 1-4 for numbers).")

        while True:

            self.print_board(self.initial_game)

            move = input("Enter your move (or 'quit' to exit): ").strip()

            if move.lower() == 'quit':

                print("Thanks for playing!")

                break

 

            try:

                row, col, num = map(int, move.split())

                if 0 <= row < 4 and 0 <= col < 4 and 1 <= num <= 4:

                    if self.is_move_valid_move(row, col, num):

                        print("Valid move! Keep up")

                        self.initial_game[row][col] = num

                        if all(self.initial_game[i][j] == self.solution[i][j] for i in range(4) for j in range(4)):

                            print("Congratulations! You solved the Sudoku.")

                            break

                    else:

                        print("Invalid move. Try again.")

                else:

                    print("Numbers must be within the grid (0-3 for rows/columns, 1-4 for numbers).")

            except ValueError:

                print("Invalid input. Please enter in the format: row column number")

 

 

if __name__ == "__main__":

    # Main script execution

    game = SudokuGame()

    game.build_game()

 

    print("Solution:")

    game.print_board(game.solution)

 

    print("\nPlayable Puzzle:")

    game.print_board(game.initial_game)

 

    game.save_to_file("sudoku.json")

    print("\nGame saved to sudoku.json")

 

    game.play_game()