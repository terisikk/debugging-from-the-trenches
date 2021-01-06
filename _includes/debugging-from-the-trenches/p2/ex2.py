class BattleShip(object):
    def __init__(self, name):
        self.name = name

ship1 = BattleShip("USS Arizona")
ship2 = BattleShip("USS California")

position = "The captain of {}."
print(position.format(ship1))

ships_available = [ship1, ship2]
print(ships_available)