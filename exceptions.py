class CustomError(Exception):
    """ This base class for all exceptions in this module"""
    pass


class EnemyDown(CustomError):
    def __str__(self):
        print('GAME OVER')


class GameOver(CustomError):
    def __str__(self):
        print("GAME OVER!")
