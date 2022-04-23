def high_and_low(numbers):
    numbers = numbers.rsplit()
    higher_value = int(numbers[0])
    lowest_value = int(numbers[0])
    for i in range(1, len(numbers)):
        if int(numbers[i]) > higher_value:
            higher_value = int(numbers[i])
        if int(numbers[i]) < lowest_value:
            lowest_value = int(numbers[i])
    numbers = ' '.join([str(higher_value), str(lowest_value)])
    return numbers

def high_and_low(numbers):
    numbers_list = [int(num) for num in sorted(numbers.split())]
    return f'{max(numbers_list)} {min(numbers_list)}'


print(high_and_low('8 3 -5 42 -1 0 0 -9 4 7 4 -4'))
