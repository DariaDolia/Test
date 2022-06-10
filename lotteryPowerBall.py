import random
AMOUNT_OF_MOST_OFTEN_NUM = 10


# first 5 numbers need to be in range [1, 69]
# the last one - is Power Ball - in range [1, 26]
def create_lottery_numbers():
    file = open('numbers.txt', 'w')
    for i in range(100):
        power_num = str(random.randint(1, 27)).zfill(2)
        for j in range(5):
            other_numbers = str(random.randint(1, 69)).zfill(2)
            file.write(f'{other_numbers} ')
        file.write(f'{power_num}\n')
    file.close()


#  create a dictionary with amount of each digits
def set_of_digits_from_file():
    file = open('numbers.txt', 'r')
    list_of_digits = []
    set_of_digit = {}
    for line in file:
        list_of_digits.extend(line.split())
    file.close()
    for digit in list_of_digits:
        if digit in set_of_digit:
            set_of_digit[digit] += 1
        else:
            set_of_digit[digit] = 1
    return set_of_digit


def sorted_the_required_numbers_of_digit(set_of_digit):
    sorted_set_of_digits = dict(sorted(set_of_digit.items(), key=lambda pair: pair[1], reverse=True))
    digits = list(sorted_set_of_digits.keys())
    amount = list(sorted_set_of_digits.values())
    try:
        for i in range(AMOUNT_OF_MOST_OFTEN_NUM):
            print(f'digits {digits[i]} appears {amount[i]} times')
    except IndexError:
        print('\nThe number of required elements is greater than the unique elements.')
        print('The maximum number of unique elements is shown.')


def main():
    create_new_lottery_numbers = input('Do you want to create a new lottery numbers? (y/n): ').lower()
    print()
    if create_new_lottery_numbers == 'y':
        create_lottery_numbers()
    set_of_all_digits = set_of_digits_from_file()
    sorted_the_required_numbers_of_digit(set_of_all_digits)


main()
