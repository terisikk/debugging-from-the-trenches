class BattleShip(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "battleship {}".format(self.name)

ship1 = BattleShip("USS Arizona")

position = "The captain of {}."
print(position.format(ship1))