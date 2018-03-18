"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest
import pdb
import isolation
import game_agent
import sample_players

from importlib import reload

TIME_LIMIT = 150


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)

    def test_example(self):
        # TODO: All methods must start with "test_"
        self.fail("Hello, World!")

    def test_minimax(self):
        minimax_player = game_agent.MinimaxPlayer(score_fn=sample_players.open_move_score)
        random_player = sample_players.RandomPlayer()
        game = isolation.Board(minimax_player, random_player)
        result = game.play(time_limit=TIME_LIMIT)
        # pdb.set_trace()
        # minimax_player.time_left = lambda : 150 

        # print(minimax_player.minimax(game,3))
    def test_alpha_beta(self):
        minimax_player = game_agent.MinimaxPlayer(score_fn=sample_players.open_move_score)
        random_player = sample_players.RandomPlayer()
        game = isolation.Board(minimax_player, random_player)
        result = game.play(time_limit=TIME_LIMIT)
        pdb.set_trace()

        


if __name__ == '__main__':
    unittest.main()
