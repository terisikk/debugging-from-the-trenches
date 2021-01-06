from pprint import pprint

class BattleShip(object):
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __repr__(self):
        return "<Battleship object: {}>".format(self.code)

ship1 = BattleShip("USS Arizona", "BB-39")
ship2 = BattleShip("USS California", "BB-44")
ship3 = BattleShip("USS Iowa", "BB-61")

patrol_shifts = [[ship1, ship2], [ship1], [ship2, ship3]]

print(patrol_shifts)
pprint(patrol_shifts)