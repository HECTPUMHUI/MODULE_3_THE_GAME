""" Let's fight begin """
from models import Enemy, Player


def get_player_name():
    """ take name for player """
    player = input('Please enter your name: ')
    return player


def play() -> None:
    """ play the game """
    player_name = get_player_name()
    player = Player(player_name)
    enemy = Enemy(5)

    while True:
        player.attack(enemy)
        player.defence(enemy)


if __name__ == '__main__':
    play()
