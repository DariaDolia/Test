def high_and_low_1(numbers):
    numbers = numbers.split()
    higher_value = int(numbers[0])
    lowest_value = int(numbers[0])
    for value in numbers[1:]:
        if int(value) > higher_value:
            higher_value = int(value)
        if int(value) < lowest_value:
            lowest_value = int(value)
    numbers = ' '.join([str(higher_value), str(lowest_value)])
    return numbers


def high_and_low_2(numbers):
    numbers += ' '
    value = ''
    high = None
    low = None
    for el in numbers:
        if el != ' ':
            value += el
            continue
        if high is None and low is None:
            high = int(value)
            low = int(value)
        if int(value) > high:
            high = int(value)
        if int(value) < low:
            low = int(value)
        value = ''
    return high, low


def high_and_low_3(numbers):
    numbers_list = [int(num) for num in numbers.split()]
    return f'{max(numbers_list)} {min(numbers_list)}'


def high_and_low_4(numbers):
    integer_list = sorted([int(el) for el in numbers.split()])
    return f'{integer_list[-1]} {integer_list[0]}'


