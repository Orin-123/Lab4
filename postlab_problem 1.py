import random
import os
import oxo_data

class Game:
    def __init__(self):
        self.board = [" "] * 9

    def new_game(self):
        """Start a new game with an empty board."""
        self.board = [" "] * 9

    def save_game(self):
        """Save the current game state."""
        oxo_data.saveGame(self.board)

    def restore_game(self):
        """Restore a saved game, or start a new game if no saved state exists."""
        try:
            game = oxo_data.restoreGame()
            if len(game) == 9:
                self.board = game
            else:
                self.new_game()
        except IOError:
            self.new_game()

    def _generate_move(self):
        """Generate a random valid move."""
        options = [i for i in range(len(self.board)) if self.board[i] == " "]
        return random.choice(options) if options else -1

    def _is_winning_move(self):
        """Check if the current board state has a winning move."""
        wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6))
        for a, b, c in wins:
            chars = self.board[a] + self.board[b] + self.board[c]
            if chars == 'XXX' or chars == 'OOO':
                return True
        return False

    def user_move(self, cell):
        """Make a move for the user."""
        if self.board[cell] != ' ':
            raise ValueError('Invalid cell')
        self.board[cell] = 'X'
        return 'X' if self._is_winning_move() else ""

    def computer_move(self):
        """Make a move for the computer."""
        cell = self._generate_move()
        if cell == -1:
            return 'D'
        self.board[cell] = 'O'
        return 'O' if self._is_winning_move() else ""

    def is_draw(self):
        """Check if the game is a draw."""
        return all(cell != " " for cell in self.board)

if __name__ == "__main__":
    # Basic test to ensure the class works as expected
    game = Game()
    game.new_game()
    print("New game:", game.board)
    game.user_move(0)
    print("After user move:", game.board)
    game.computer_move()
    print("After computer move:", game.board)
