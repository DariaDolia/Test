def sorting(massive):
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


print(sorting([0, 1, 9, 2, 4, 3, 6, 5]))
