def main():
    num_list = [4, 16, 0, 12, 11]
    print(max_val(num_list))


def max_val(num_list):
    if len(num_list) == 1:
        return num_list[0]
    maximum = max_val(num_list[1:])
    return max(num_list[0], maximum)


main()
