def step_per_month(position, days):
    file = open('steps.txt', 'r')
    total = 0
    file.seek(position)
    step = file.readline()
    next_position = 0
    for i in range(days):
        next_position += len(step)
        total += int(step.rstrip('\n'))
        step = file.readline()
    average = int(total / days)
    file.close()
    return average, next_position


def main():
    january, next_position = step_per_month(0, 31)
    february, next_position = step_per_month(next_position, 28)
    march, next_position = step_per_month(next_position, 31)
    april, next_position = step_per_month(next_position, 30)
    may, next_position = step_per_month(next_position, 31)
    june, next_position = step_per_month(next_position, 30)
    july, next_position = step_per_month(next_position, 31)
    august, next_position = step_per_month(next_position, 31)
    september, next_position = step_per_month(next_position, 30)
    october, next_position = step_per_month(next_position, 31)
    november, next_position = step_per_month(next_position, 30)
    december, next_position = step_per_month(next_position, 31)

    dictionary = {'January': january, 'February': february, 'March': march,
                  'April': april, 'May': may, 'June': june, 'July': july,
                  'August': august, 'September': september, 'October': october,
                  'November': november, 'December': december}
    for i, j in dictionary.items():
        print(f'Average steps for {i} is {j}')


main()
