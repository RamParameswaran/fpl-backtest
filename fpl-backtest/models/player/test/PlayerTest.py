import unittest

from .. import Player


class PlayerTest(unittest.TestCase):
    def test_instantiate(self):
        player = Player.Player(player_id=72, name="Aaron_Connolly")
        self.assertIsNotNone(player)  # add assertion here

    def test_equals(self):
        player1 = Player.Player(player_id=72, name="Aaron_Connolly")
        player2 = Player.Player(player_id=72, name="Some_Different_Name")
        player3 = Player.Player(player_id=999, name="Aaron_Connolly")

        self.assertEquals(player1, player2)
        self.assertNotEquals(player1, player3)


if __name__ == '__main__':
    unittest.main()
