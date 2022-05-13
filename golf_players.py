def choice_of_option():
    while True:
        print('If you wanna write a player\'s result press 1')
        print('If you wanna leave the program press 2')
        try:
            choice = int(input('\nEnter 1 or 2: '))
            return choice
        except ValueError:
            print('You entered letters.\n')
            continue


def player_name():
    while True:
        name_of_player = input('Enter a name of player: ')
        if name_of_player.strip() == '':
            print('Please, enter a name\n')
            continue
        else:
            return name_of_player


def player_score():
    while True:
        try:
            game_score = int(input('Enter a score of the player: '))
            print()
            return game_score
        except ValueError:
            print('Enter only integer numbers\n')
            continue


def main():
    while True:
        choice = choice_of_option()
        if choice == 1:
            name_of_player = player_name()
            game_score = player_score()
            file = open('golf.txt', 'a')
            file.write(name_of_player + '\n')
            file.write(str(game_score) + '\n')
            print('The data was writen in the file\n')
        elif choice == 2:
            file.close()
            break
        else:
            print('You value out of range. Try again.\n')


main()
