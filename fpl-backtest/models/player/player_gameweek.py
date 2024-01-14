import datetime


class PlayerGameweek:
    player_id: int
    season: str
    round: int
    opponent_team_id: int
    team_a_score: int
    team_h_score: int

    assists: int
    bonus: int
    bps: int
    clean_sheets: int
    creativity: float
    expected_assists: float
    expected_goal_involvements: float
    expected_goals: float
    expected_goals_conceded: float
    goals_conceded: int
    goals_scored: int
    ict_index: int
    influence: int
    kickoff_time: datetime.datetime
    minutes: int
    own_goals: int
    penalties_missed: int
    penalties_saved: int
    red_cards: int
    saves: int
    selected: int
    starts: int
    threat: float
    total_points: int
    transfers_balance: int
    transfers_in: int
    transfers_out: int
    value: int
    was_home: bool
    yellow_cards: int

    def __init__(self, player_id: int, season: str,
                 opponent_team_id: int = 0,
                 assists: int = 0,
                 bonus: int = 0,
                 bps: int = 0,
                 clean_sheets: int = 0,
                 creativity: float = 0.0,
                 expected_assists: float = 0.0,
                 expected_goal_involvements: float = 0.0,
                 expected_goals: float = 0.0,
                 expected_goals_conceded: float = 0.0,
                 goals_conceded: int = 0,
                 goals_scored: int = 0,
                 ict_index: int = 0,
                 influence: int = 0,
                 kickoff_time: datetime.datetime = None,
                 minutes: int = 0,
                 own_goals: int = 0,
                 penalties_missed: int = 0,
                 penalties_saved: int = 0,
                 red_cards: int = 0,
                 round: int = 0,
                 saves: int = 0,
                 selected: int = 0,
                 starts: int = 0,
                 team_a_score: int = 0,
                 team_h_score: int = 0,
                 threat: float = 0.0,
                 total_points: int = 0,
                 transfers_balance: int = 0,
                 transfers_in: int = 0,
                 transfers_out: int = 0,
                 value: int = 0,
                 was_home: bool = None,
                 yellow_cards: int = 0
                 ) -> None:
        self.player_id = player_id
        self.season = season
        self.round = round
        self.team_a_score = team_a_score
        self.team_h_score = team_h_score

        self.opponent_team_id = opponent_team_id
        self.assists = assists
        self.bonus = bonus
        self.bps = bps
        self.clean_sheets = clean_sheets
        self.creativity = creativity
        self.expected_assists = expected_assists
        self.expected_goal_involvements = expected_goal_involvements
        self.expected_goals = expected_goals
        self.expected_goals_conceded = expected_goals_conceded
        self.goals_conceded = goals_conceded
        self.goals_scored = goals_scored
        self.ict_index = ict_index
        self.influence = influence
        self.kickoff_time = kickoff_time
        self.minutes = minutes
        self.own_goals = own_goals
        self.penalties_missed = penalties_missed
        self.penalties_saved = penalties_saved
        self.red_cards = red_cards
        self.saves = saves
        self.selected = selected
        self.starts = starts
        self.threat = threat
        self.total_points = total_points
        self.transfers_balance = transfers_balance
        self.transfers_in = transfers_in
        self.transfers_out = transfers_out
        self.value = value
        self.was_home = was_home
        self.yellow_cards = yellow_cards

    def __eq__(self, other):
        if not isinstance(other, PlayerGameweek):
            return NotImplemented
        player_ids_equal = self.player_id == other.player_id
        season_equal = self.season == other.season
        round_equal = self.round == other.round
        if player_ids_equal and season_equal and round_equal:
            return True
        else:
            return False
