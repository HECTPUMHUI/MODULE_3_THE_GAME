from settings import INITIAL_PLAYER_HEALTH

"""
 Model of players

"""


class Enemy:
    def __init__(self, level: int):
        self.level = level

    def decrease_health(self):
        self.level -= self.level
        return self.level

    def select_attack(self):
        ...

    def select_defence(self):
        ...


class Player:
    def __init__(self, name: str, health_point=INITIAL_PLAYER_HEALTH):
        self.name = name
        self.health_point = health_point

    def decrease_health(self):
        if self.health_point != 0:
            result = self.health_point - 1
            self.health_point = result
        if self.health_point == 0:
            print(f'Game over! << exception >>')
        return self.health_point

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


user_1 = Player('Jimmy')
print(f'{user_1.name = }')
print(f'{user_1.health_point = }')
enemy_1 = Enemy(10)
print(f'{enemy_1.level = }')
print(user_1.decrease_health())
print(user_1.decrease_health())
print(user_1.decrease_health())
print(user_1.decrease_health())
print(user_1.decrease_health())
