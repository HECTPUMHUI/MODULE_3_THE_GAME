"""
 Model of players and enemy's

"""
from random import randint

import settings


class Enemy:
    """ Create a new enemy  """

    def __init__(self, level: int):
        self.level = level

    def __str__(self):
        return f'{self.level = }'

    def decrease_health(self):
        """ decrease health """
        self.level -= 1
        return self.level

    def select_attack(self):
        """ enemy random attack """
        enemy_attack = int(randint(1, 3))
        return enemy_attack

    def select_defence(self):
        """ enemy random defence """
        enemy_defence = int(randint(1, 3))
        return enemy_defence


class Player:
    """ Create a new player """

    def __init__(self, name: str, health_point=settings.INITIAL_PLAYER_HEALTH):
        self.name = name
        self.health_point = health_point
        self.PLAYER_SCORE = 0

    def decrease_health(self):
        """ decrease health """
        self.health_point -= 1
        return self.health_point

    def select_attack(self, user_attack):
        """ select attack """
        user_attack = int(input("\nPlease enter your attack:"
                                "\n\t WARRIOR = 1\tROBBER = 2\tWIZARD = 3\n "))
        return user_attack

    def select_defence(self, user_defence):
        """ select defence """
        user_defence = int(input("\nPlease enter your defence:"
                                 "\n\t WARRIOR = 1\tROBBER = 2\tWIZARD = 3\n "))
        return user_defence

    def fight(self, user_attack, user_defence, enemy: Enemy):
        """ fight a player """
        if user_attack == 1:
            if enemy.select_defence == 1:
                print("IT'S A DRAW!")
            elif enemy.select_defence == 2:
                print("YOUR ATTACK IS SUCCESSFUL!")
                settings.ENEMY_HEALTH_LEVEL -= 1
                self.PLAYER_SCORE += 1
            elif enemy.select_defence == 3:
                print("YOUR ATTACK IS FAILED!")

        if user_attack == 2:
            if enemy.select_defence == 1:
                print("YOUR ATTACK IS FAILED!")
            elif enemy.select_defence == 2:
                print("IT'S A DRAW!")
            elif enemy.select_defence == 3:
                print("YOUR ATTACK IS SUCCESSFUL!")
                settings.ENEMY_HEALTH_LEVEL -= 1
                self.PLAYER_SCORE += 1

        if user_attack == 3:
            if enemy.select_defence == 1:
                print("YOUR ATTACK IS SUCCESSFUL!")
                settings.ENEMY_HEALTH_LEVEL -= 1
                self.PLAYER_SCORE += 1
            elif enemy.select_defence == 2:
                print("YOUR ATTACK IS FAILED!")
            elif enemy.select_defence == 3:
                print("IT'S A DRAW!")

        if enemy.select_attack == 1:
            if user_defence == 1:
                print("IT'S A DRAW!")
            elif user_defence == 2:
                print("YOUR DEFENCE IS FAILED!")
                settings.PLAYER_HEALTH_LEVEL -= 1
            elif user_defence == 3:
                print("YOUR DEFENCE IS SUCCESSFUL!")

        if enemy.select_attack == 2:
            if user_defence == 1:
                print("YOUR DEFENCE IS SUCCESSFUL!")
            elif user_defence == 2:
                print("IT'S A DRAW!")
            elif user_defence == 3:
                print("YOUR DEFENCE IS FAILED!")
                settings.PLAYER_HEALTH_LEVEL -= 1

        if enemy.select_attack == 3:
            if user_defence == 1:
                print("YOUR DEFENCE IS FAILED!")
                settings.PLAYER_HEALTH_LEVEL -= 1
            elif user_defence == 2:
                print("YOUR DEFENCE IS SUCCESSFUL!")
            elif user_defence == 3:
                print("IT'S A DRAW!")

    def attack(self, user_attack):
        """Attack"""
        return user_attack

    def defence(self, user_defence):
        """Defense"""
        return user_defence


user_1 = Player('Jimmy')
# print(f'{user_1.name = }')
# print(f'{user_1.health_point = }')
enemy_1 = Enemy(10)
# print(f'{enemy_1.level = }')
print(user_1.PLAYER_SCORE)
A1 = user_1.select_defence(2)
A2 = user_1.select_attack(1)

print(user_1.PLAYER_SCORE)
print(A1)
print(A2)
print(enemy_1)
print(f"{enemy_1.select_attack() = }")
print(f"{enemy_1.select_defence() = }")
print(f"{user_1.name = }")
print(f"{user_1.health_point = }")
user_1.decrease_health()
user_1.decrease_health()
print(f"{user_1.health_point = }")
print(user_1.fight(A1, A2, enemy_1))
