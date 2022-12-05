"""
 Model of players

"""


class Enemy:
    def __init__(self, level: int):
        self.level = level

    def decrease_health(self):
        ...

    def select_attack(self):
        ...

    def select_defence(self):
        ...


class Player:
    def __init__(self, name: str, health_point=0):
        self.name = name
        self.health_point = health_point

    def decrease_health(self):
        ...

    def select_attack(self):
        ...

    def select_defence(self):
        ...

    def fight(self):
        ...

    def attack(self):
        ...

    def defence(self):
        ...
