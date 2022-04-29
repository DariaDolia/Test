import random


def create_massive():
    num = list(range(1, 16))
    num.append(' ')
    mas = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(4):
        for j in range(4):
            mas[i][j] = random.choice(num)
            num.remove(mas[i][j])
    return mas


def puzzle_field(massive):
    print('---------------------')
    for i in range(4):
        for j in range(4):
            print(f'|{massive[i][j]:3}', end=' ')
        print('|')
        print('---------------------')


def shift_left(massive):
    for i in range(4):
        for j in range(4):
            if massive[i][j] == ' ':
                left_element = massive[i][j - 1]
                if 0 < j <= 3:
                    massive[i][j - 1] = ' '
                    massive[i][j] = left_element
    return massive


def shift_right(massive):
    for i in range(4):
        for j in range(2, -1, -1):
            if massive[i][j] == ' ':
                right_element = massive[i][j + 1]
                if 0 <= j < 3:
                    massive[i][j + 1] = ' '
                    massive[i][j] = right_element
    return massive


def shift_up(massive):
    for i in range(4):
        for j in range(4):
            if massive[i][j] == ' ':
                up_element = massive[i - 1][j]
                if 0 < i <= 3:
                    massive[i - 1][j] = ' '
                    massive[i][j] = up_element
    return massive


def shift_down(massive):
    for i in range(2, -1, -1):
        for j in range(4):
            if massive[i][j] == ' ':
                down_element = massive[i + 1][j]
                if 0 <= i < 3:
                    massive[i + 1][j] = ' '
                    massive[i][j] = down_element
    return massive


def instruction():
    print('press 1 to shift left')
    print('press 2 to shift right')
    print('press 3 to shift up')
    print('press 4 to shift down')
    print('press 5 to end the game')


def check_choice():
    while True:
        try:
            choice = int(input('\nEnter your option: '))
            return choice
        except ValueError:
            print('Invalid value. Try again')


def main():
    massive = create_massive()
    puzzle_field(massive)
    print()
    while True:
        instruction()
        choice = check_choice()
        if choice == 1:
            new_massive = shift_left(massive)
        elif choice == 2:
            new_massive = shift_right(massive)
        elif choice == 3:
            new_massive = shift_up(massive)
        elif choice == 4:
            new_massive = shift_down(massive)
        elif choice == 5:
            break
        puzzle_field(new_massive)


main()
