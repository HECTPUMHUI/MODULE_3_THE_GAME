""" Let's fight begin """
from exceptions import EnemyDown, GameOver
from models import Enemy, Player


def get_player_name():
    """ take name for player """
    player = input('Please enter your name: ')
    return player


def watch_scores():
    score_file = open("file_with_score.txt", "r")
    print(score_file.read())


def play() -> None:
    """ play the game """
    player_name = get_player_name()
    player = Player(player_name)
    enemy = Enemy(5)
    score_list = []
    print(f'{enemy.health_point = }')

    while True:
        just_do_it = input('AVAILABLE MENU CHOICES: PLAY, SCORES, EXIT\n'
                           'TYPE YOUR CHOICE HERE: ')
        if just_do_it == 'SCORES':
            watch_scores()
            continue
        if just_do_it == 'EXIT':
            break
        if just_do_it == 'PLAY':
            while True:
                try:
                    player.attack(enemy)
                    player.defence(enemy)
                except EnemyDown:
                    player.score += 5
                    print(f'You WIN! \n>>>Your score: {player.score}')
                    score_list.append(player.name)
                    score_list.append(player.score)
                    with open("file_with_score.txt", "a") as file:
                        print(*score_list, file=file, sep=' \n')
                    enemy = Enemy(enemy.level + 1)
                    continue
                except GameOver:
                    print(f'GAME OVER! \n>>>Enemy level: {enemy.level} \n'
                          f'>>>Your score: {player.score}')
                    score_list.append(player.name)
                    score_list.append(player.score)
                    break


if __name__ == '__main__':
    try:
        play()
    except KeyboardInterrupt:
        print('EMERGENCY EXIT')
