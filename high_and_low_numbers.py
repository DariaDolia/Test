def high_and_low(numbers):
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

def high_and_low(numbers):
    numbers_list = [int(num) for num in numbers.split()]
    return f'{max(numbers_list)} {min(numbers_list)}'

def high_and_low(numbers):
    integer_list = [int(el) for el in numbers.split()]
    return f'{sorted(integer_list)[-1]} {sorted(integer_list)[0]}'


print(high_and_low('8 3 -5 42 -1 0 0 -9 4 7 4 -4'))
