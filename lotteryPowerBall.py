import random
AMOUNT_OF_MOST_OFTEN_NUM = 5


#  changes number from 1 to 9 in format
#  with 0 in the beginning (task requirement)
def change_number_format(num):
    if num in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        num = f'0{num}'
    return num


# first 5 numbers need to be in range [1, 69]
# the last one - is Power Ball - in range [1, 26]
def create_lottery_numbers():
    file = open('numbers.txt', 'w')
    for i in range(100):
        power_num = change_number_format(random.randint(1, 27))
        for j in range(5):
            num = change_number_format(random.randint(1, 70))
            file.write(f'{num} ')
        file.write(f'{power_num}\n')
    file.close()


#  create a dictionary with amount of each digits
def set_of_digits_from_file():
    file = open('numbers.txt', 'r')
    list_of_digits = []
    for line in file:
        list_of_digits.extend(line.split())
    file.close()
    return {digit: list_of_digits.count(digit) for digit in list_of_digits}


# create dictionary with only the most often numbers
def most_often_numbers(set_of_all_digits):
    max_values = sorted(set_of_all_digits.values(), reverse=True)[:AMOUNT_OF_MOST_OFTEN_NUM]
    list_of_numbers = {}
    for k, v in set_of_all_digits.items():
        if max_values:
            if v in max_values:
                list_of_numbers[k] = v
                max_values.remove(v)
        else:
            break
    return list_of_numbers


def sorted_the_most_often_numbers(numbers_set):
    max_values = sorted(numbers_set.values(), reverse=True)
    while True:
        for k, v in numbers_set.items():
            if not max_values:
                return
            if v == max_values[0]:
                print(f'digit {k} appears {v} times')
                del max_values[0]


def main():
    create_new_lottery_numbers = input('Do you want to create a new lottery numbers? (y/n): ').lower()
    if create_new_lottery_numbers == 'y':
        create_lottery_numbers()
    set_of_all_digits = set_of_digits_from_file()
    numbers_set = most_often_numbers(set_of_all_digits)
    sorted_the_most_often_numbers(numbers_set)


main()
