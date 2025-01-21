
import unittest
from PostLab1 import Game

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        """Set up a new game instance for testing."""
        self.game = Game()
        self.game.new_game()

    def test_new_game(self):
        """Test that a new game starts with an empty board."""
        self.assertEqual(self.game.board, [" "] * 9)

    def test_user_move(self):
        """Test that a user move updates the board correctly."""
        self.game.user_move(0)
        self.assertEqual(self.game.board[0], 'X')

    def test_invalid_user_move(self):
        """Test that a ValueError is raised for an invalid move."""
        self.game.user_move(0)
        with self.assertRaises(ValueError):
            self.game.user_move(0)

    def test_computer_move(self):
        """Test that a computer move updates the board correctly."""
        self.game.computer_move()
        self.assertIn('O', self.game.board)

    def test_draw_game(self):
        """Test that the game correctly identifies a draw."""
        self.game.board = ['X', 'O', 'X',
                           'X', 'X', 'O',
                           'O', 'X', 'O']
        self.assertTrue(self.game.is_draw())

    def test_winning_move(self):
        """Test that the game correctly identifies a winning move."""
        self.game.board = ['X', 'X', ' ',
                           'O', 'O', ' ',
                           ' ', ' ', ' ']
        self.game.user_move(2)
        self.assertTrue(self.game._is_winning_move())

if __name__ == "__main__":
    unittest.main()
