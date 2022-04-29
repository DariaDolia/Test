# def high_and_low_1(numbers):
#     numbers = numbers.split()
#     higher_value = int(numbers[0])
#     lowest_value = int(numbers[0])
#     for value in numbers[1:]:
#         if int(value) > higher_value:
#             higher_value = int(value)
#         if int(value) < lowest_value:
#             lowest_value = int(value)
#     numbers = ' '.join([str(higher_value), str(lowest_value)])
#     return numbers

def high_and_low_2(numbers):
    numbers += ' '
    value = ''
    massive_for_determine_max_min = []
    count = 0
    for el in numbers:
        if el != ' ':
            value += el
        else:
            if count < 2:
                massive_for_determine_max_min.append(int(value))
                if len(massive_for_determine_max_min) == 2:
                    if massive_for_determine_max_min[0] > massive_for_determine_max_min[1]:
                        high = massive_for_determine_max_min[0]
                        low = massive_for_determine_max_min[1]
                    else:
                        high = massive_for_determine_max_min[1]
                        low = massive_for_determine_max_min[0]
            if count >= 2:
                if int(value) > high:
                    high = int(value)
                if int(value) < low:
                    low = int(value)
            count += 1
            value = ''
    return high, low

# def high_and_low_3(numbers):
#     numbers_list = [int(num) for num in numbers.split()]
#     return f'{max(numbers_list)} {min(numbers_list)}'

# def high_and_low_4(numbers):
#     integer_list = sorted([int(el) for el in numbers.split()])
#     return f'{integer_list[-1]} {integer_list[0]}'


print(high_and_low_2('0 -5 -3 -11 -4'))

# '8 3 -5 42 -1 0 0 -9 4 7 4 -4'

