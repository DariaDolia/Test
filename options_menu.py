
def options():
    while True:
        print()
        print('1) Get your IP address')
        print('2) Get weather in the city')
        print('3) Terminate\n')

        try:
            chosen_option = int(input('Choose an option: '))
            return chosen_option
        except ValueError:
            print('Invalid value. Enter a number from the list\n')