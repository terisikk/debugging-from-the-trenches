class BattleShip(object):
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __repr__(self):
        return "<Battleship object: {}>".format(self.code)

ship1 = BattleShip("USS Arizona", "BB-39")
ship2 = BattleShip("USS California", "BB-44")

ships_available = [ship1, ship2]
print(ships_available)