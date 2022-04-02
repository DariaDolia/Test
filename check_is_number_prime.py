def get_number():
    while True:
        try:
            number = int(input('\nВведите натуральное число: '))
        except ValueError:
            print('Введено некоректоное значение.')
            print('Введите натуральное число.')
            continue
        if number == 0 or number == 1:
            print('Это число не является ни простым, ни составным')
        elif number < 0:
            print('Простое число может быть только натуральным.')
            print('То есть необходимо ввести целое, положительное число.')
        else:
             return number


def is_prime(number):
    status = True    
    for divisor in range(2, number):
        if number % divisor == 0:
            status = False
            break
    return status


def main():
    again = 1
    while again != '0':
        value = get_number()
        if is_prime(value):
            print(f'Число {value} - простое')
        else:
            print(f'Число {value} - составное')
        print('\nЕсли вы хотите проверить еще одно число - нажмите Enter.')
        print('Если хотите завершить - введите 0.')
        again = input()


main()
