""" This my exceptions """


class CustomError(Exception):
    """ This base class for all exceptions in this module"""


class EnemyDown(CustomError):
    """ This class exception where the enemy is down"""


class GameOver(CustomError):
    """ This class exception where the game is over and player is dead"""
