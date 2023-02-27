def sum_two_num(mas, k):
    start = 0
    end = len(mas) - 1
    while start != end:
        summa = mas[start] + mas[end]
        if summa == k:
            print(f'Answer: {mas[start]} and {mas[end]}')
            return
        elif summa > k:
            end -= 1
        else:
            start += 1
    print([])


sum_two_num([-1, 4, 7, 7, 7], 3)
