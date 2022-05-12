import random


def create_massive():
    num = list(range(1, 16))
    num.append(' ')
    massive = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(4):
        for j in range(4):
            massive[i][j] = random.choice(num)
            num.remove(massive[i][j])
    return massive


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
    finish_x = x + x_change
    finish_y = y + y_change
    if 0 <= finish_x <= 3 and 0 <= finish_y <= 3:
        element = massive[finish_y][finish_x]
        massive[finish_y][finish_x] = ' '
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
            new_massive = shift(massive, -1, 0)
        elif choice == 2:
            new_massive = shift(massive, 1, 0)
        elif choice == 3:
            new_massive = shift(massive, 0, -1)
        elif choice == 4:
            new_massive = shift(massive, 0, 1)
        if choice == 5:
            break
        puzzle_field(new_massive)


main()
