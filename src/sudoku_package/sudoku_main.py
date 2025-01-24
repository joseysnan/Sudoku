
   
from sudoku_game import SudokuGame
import random 

if __name__ == "__main__":
    game = SudokuGame()
    game.build_game()
    print("Solution:")
    game.print_board(game.solution)
    print("\nPlayable Puzzle:")
    game.print_board(game.initial_game)
    game.save_to_file("sudoku.json")
    game.play_game()

