import datetime
import unittest

from .. import PlayerGameweek


class PlayerGameweekTest(unittest.TestCase):

    def test_instantiate_with_default_values(self):
        pgw = build_empty_playergameweek()
        self.assertIsNotNone(pgw)

    def test_instantiate_with_all_variables_filled(self):
        pgw = build_full_playergameweek()
        for attr, value in pgw.__dict__.items():
            self.assertNotIn(value, [0, 0.0, None], "Found a default value")

    def test_eq_method(self):
        empty_object = build_empty_playergameweek()
        full_object = build_full_playergameweek()
        modified_object = build_full_playergameweek()
        modified_object.player_id = 999

        self.assertEquals(empty_object, full_object)
        self.assertNotEquals(empty_object, modified_object)


def build_empty_playergameweek():
    return PlayerGameweek.PlayerGameweek(player_id=1, season="2022-23", round=1)


def build_full_playergameweek():
    return PlayerGameweek.PlayerGameweek(player_id=1, season="2022-23", round=1,
                                         opponent_team_id=1,
                                         assists=1,
                                         bonus=1,
                                         bps=1,
                                         clean_sheets=1,
                                         creativity=1.1,
                                         expected_assists=1.1,
                                         expected_goal_involvements=1.1,
                                         expected_goals=1.1,
                                         expected_goals_conceded=1.1,
                                         goals_conceded=1,
                                         goals_scored=1,
                                         ict_index=1,
                                         influence=1,
                                         kickoff_time=datetime.datetime.now(),
                                         minutes=1,
                                         own_goals=1,
                                         penalties_missed=1,
                                         penalties_saved=1,
                                         red_cards=1,
                                         saves=1,
                                         selected=1,
                                         starts=1,
                                         team_a_score=1,
                                         team_h_score=1,
                                         threat=1.1,
                                         total_points=1,
                                         transfers_balance=1,
                                         transfers_in=1,
                                         transfers_out=1,
                                         value=1,
                                         was_home=True,
                                         yellow_cards=1
                                         )


if __name__ == '__main__':
    unittest.main()
