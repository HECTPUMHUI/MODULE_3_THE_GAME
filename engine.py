""" Let's fight begin """
from exceptions import EnemyDown, GameOver
from models import Enemy, Player
from settings import ENEMY_HEALTH_LEVEL


def get_player_name():
    """ take name for player """
    player = input('Please enter your name: ')
    return player


def watch_scores():
    """ watch scores in file """
    score_file = open("file_with_score.txt", "r")
    print(score_file.read())


def save_scores(list):
    """ save scores in file """
    with open("file_with_score.txt", "a") as file:
        print(*list, file=file, sep=' \n')


def play() -> None:
    """ play the game """
    player_name = get_player_name()
    player = Player(player_name)
    enemy = Enemy(ENEMY_HEALTH_LEVEL)
    score_list = []

    while True:
        try:
            player.attack(enemy)
            player.defence(enemy)
        except EnemyDown:
            player.score += 5
            print(f'You WIN! \n>>>Your score: {player.score}')
            score_list.append(player)
            save_scores(score_list)
            enemy = Enemy(enemy.level + 1)
        except GameOver:
            print(f'GAME OVER! \n>>>Enemy level: {enemy.level} \n'
                  f'>>>Your score: {player.score}')
            break


if __name__ == '__main__':
    try:
        play()
    except KeyboardInterrupt:
        print('EMERGENCY EXIT')
