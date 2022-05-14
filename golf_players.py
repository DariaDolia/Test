def check_numbers(check_is_integer, error_message):
    try:
        number = int(check_is_integer)
        return number
    except ValueError:
        print(error_message)


def choice_of_option():
    while True:
        print('If you wanna write a player\'s result press 1')
        print('If you wanna leave the program press 2')
        number = input('\nEnter 1 or 2: ')
        number = check_numbers(number, 'You entered letters or nothing.\n')
        if number is not None:
            return number


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
        game_score = input('Enter a score of the player: ')
        score = check_numbers(game_score, 'Enter only integer numbers\n')
        if score is not None:
            return game_score


def main():
    while True:
        choice = choice_of_option()
        if choice == 1:
            name_of_player = player_name()
            game_score = player_score()
            file = open('golf.txt', 'a')
            file.write(f'{name_of_player}\n')
            file.write(f'{game_score}\n')
            print('\nThe data was writen in the file\n')
            file.close()
        elif choice == 2:
            print('\nYou stoped the program')
            break
        else:
            print('You value out of range. Try again.\n')


main()
