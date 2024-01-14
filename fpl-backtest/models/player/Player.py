from . import PlayerGameweek


class Player(object):
    player_id: int
    name: str
    gameweeks: set[PlayerGameweek]

    def __init__(self, player_id: int, name: str):
        self.player_id = player_id
        self.name = name
        self.gameweeks = set()

    def add_gameweek(self, gameweek: PlayerGameweek) -> None:
        self.gameweeks.add(gameweek)

    def __eq__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        return self.player_id == other.player_id
