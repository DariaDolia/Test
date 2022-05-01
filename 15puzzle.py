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


def coordinate(massive):
    for y in range(4):
        for x in range(4):
            if massive[y][x] == ' ':
                return x, y


def shift(massive, x_change, y_change):
    x, y = coordinate(massive)
    if x_change == 1:
        x_change = x - 1
        y_change = y
    elif x_change == 2:
        x_change = x + 1
        y_change = y
    elif y_change == 3:
        x_change = x
        y_change = y - 1
    elif y_change == 4:
        x_change = x
        y_change = y + 1
    if 0 <= x_change <= 3 and 0 <= y_change <= 3:
        element = massive[y_change][x_change]
        massive[y_change][x_change] = ' '
        massive[y][x] = element
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
        except ValueError:
            print('Invalid value. Try again')
            continue
        if choice not in [1, 2, 3, 4, 5]:
            print('Number out of range. Enter a number from 1 till 5. ')
        else:
            return choice


def main():
    massive = create_massive()
    puzzle_field(massive)
    print()
    while True:
        instruction()
        choice = check_choice()
        if choice == 1:
            new_massive = shift(massive, 1, 0)
        elif choice == 2:
            new_massive = shift(massive, 2, 0)
        elif choice == 3:
            new_massive = shift(massive, 0, 3)
        elif choice == 4:
            new_massive = shift(massive, 0, 4)
        if choice == 5:
            break
        puzzle_field(new_massive)


main()
