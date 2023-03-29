import options_menu


def main():
    chosen_option = 1
    while chosen_option != 3:
        chosen_option = options_menu.options()
        res = options_menu.Result
        res.show_result(chosen_option)


if __name__ == '__main__':
    main()
