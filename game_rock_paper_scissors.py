import random

options = ['камень', 'ножницы', 'бумага']


def user_choice():
    while True:
        user_option = input('\nВведите один из вариантов: камень, ножницы, бумага: ').lower()
        if user_option not in options:
            print('Некоректное значение. Повторите попытку')
        else:
            return user_option


def winner(computer, user):
    if computer == 'камень' and user == 'ножницы':
        print('\nПобедил компьютер, так как камень разбивает ножницы')
    elif computer == 'ножницы' and user == 'бумага':
        print('\nПобедил компьютер, так как ножницы режут бумагу')
    elif computer == 'бумага' and user == 'камень':
        print('\nПобедил компьютер, так как бумага заворачивает камень')
    elif user == 'камень' and computer == 'ножницы':
        print('\nВы победили, так как камень разбивает ножницы')
    elif user == 'ножницы' and computer == 'бумага':
        print('\nВы победили, так как ножницы режут бумагу')
    elif user == 'бумага' and computer == 'камень':
        print('\nВы победили, так как бумага заворачивает камень')


def repeat_game():
    while True:
        print('\nВы хотите продолжить игру?')
        again = input('Введите да или нет: ').lower()
        if again not in ['да', 'нет']:
            print('\nВы ввели некорректное значение.')
            print('Повторите попытку.')
        else:
            return again


def main():
    again = 'да'
    while again == 'да':
        while True:
            user = user_choice()
            computer = options[random.randint(0, 2)]  # рандомный выбор компьютера
            print(f'Выбор компьютера: {computer}')
            if user != computer:
                break
            print('\nНичья. Играем повторный раунд')
        winner(computer, user)
        again = repeat_game()


main()
