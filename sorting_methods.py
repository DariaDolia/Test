def selection_sorts(massive):
    n = len(massive)
    for i in range(n - 1):
        k = i
        maximum = massive[i]
        for j in range(i + 1, n):
            if massive[j] > maximum:
                k = j
                maximum = massive[j]
        massive[k] = massive[i]
        massive[i] = maximum
    return massive


print(selection_sorts([0, 1, 9, 2, 4, 3, 6, 5]))


def bubble_sort(massive):
    n = len(massive)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            compared_element = massive[j]
            if massive[j] < massive[j + 1]:
                massive[j] = massive[j + 1]
                massive[j + 1] = compared_element
    return massive


print(bubble_sort([0, 1, 9, -9, 4, 3, 6, 5]))



