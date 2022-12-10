from random import randint

import settings

"""
 Model of players and enemy's

"""


class Enemy:
    """ Create a new enemy  """

    def __init__(self, level: int):
        self.level = level

    def decrease_health(self):
        self.level -= self.level
        return self.level

    def select_attack(self):
        ENEMY_DEFENCE = int(randint(1, 3))
        return ENEMY_DEFENCE

    def select_defence(self):
        ENEMY_ATTACK = int(randint(1, 3))
        return ENEMY_ATTACK


class Player:
    """ Create a new player """

    def __init__(self, name: str, health_point=settings.INITIAL_PLAYER_HEALTH):
        self.name = name
        self.health_point = health_point

    def decrease_health(self):
        result = self.health_point
        result -= 1
        return result

    def select_attack(self, user_attack):
        return user_attack

    def select_defence(self, user_defence):
        return user_defence

    def fight(self, user_attack, ENEMY_DEFENCE, user_defence, ENEMY_ATTACK):
        if user_attack == 1:
            if ENEMY_DEFENCE == 1:
                print("IT'S A DRAW!")
            elif ENEMY_DEFENCE == 2:
                print("YOUR ATTACK IS SUCCESSFUL!")
                settings.ENEMY_HEALTH_LEVEL -= 1
                settings.PLAYER_SCORE += 1
            elif ENEMY_DEFENCE == 3:
                print("YOUR ATTACK IS FAILED!")

        if user_attack == 2:
            if ENEMY_DEFENCE == 1:
                print("YOUR ATTACK IS FAILED!")
            elif ENEMY_DEFENCE == 2:
                print("IT'S A DRAW!")
            elif ENEMY_DEFENCE == 3:
                print("YOUR ATTACK IS SUCCESSFUL!")
                settings.ENEMY_HEALTH_LEVEL -= 1
                settings.PLAYER_SCORE += 1

        if user_attack == 3:
            if ENEMY_DEFENCE == 1:
                print("YOUR ATTACK IS SUCCESSFUL!")
                settings.ENEMY_HEALTH_LEVEL -= 1
                settings.PLAYER_SCORE += 1
            elif ENEMY_DEFENCE == 2:
                print("YOUR ATTACK IS FAILED!")
            elif ENEMY_DEFENCE == 3:
                print("IT'S A DRAW!")

        if ENEMY_ATTACK == 1:
            if user_defence == 1:
                print("IT'S A DRAW!")
            elif user_defence == 2:
                print("YOUR DEFENCE IS FAILED!")
                settings.PLAYER_HEALTH_LEVEL -= 1
            elif user_defence == 3:
                print("YOUR DEFENCE IS SUCCESSFUL!")

        if ENEMY_ATTACK == 2:
            if user_defence == 1:
                print("YOUR DEFENCE IS SUCCESSFUL!")
            elif user_defence == 2:
                print("IT'S A DRAW!")
            elif user_defence == 3:
                print("YOUR DEFENCE IS FAILED!")
                settings.PLAYER_HEALTH_LEVEL -= 1

        if ENEMY_ATTACK == 3:
            if ENEMY_DEFENCE == 1:
                print("YOUR DEFENCE IS FAILED!")
                settings.PLAYER_HEALTH_LEVEL -= 1
            elif ENEMY_DEFENCE == 2:
                print("YOUR DEFENCE IS SUCCESSFUL!")
            elif ENEMY_DEFENCE == 3:
                print("IT'S A DRAW!")

    def attack(self, user_attack):
        return user_attack

    def defence(self, user_defence):
        return user_defence


user_1 = Player('Jimmy')
print(f'{user_1.name = }')
print(f'{user_1.health_point = }')
enemy_1 = Enemy(10)
print(f'{enemy_1.level = }')
e1 = enemy_1.select_attack()
e2 = enemy_1.select_defence()
a1 = user_1.select_defence(2)
a2 = user_1.select_attack(1)
user_1.fight(a1, e1, a2, e2)
