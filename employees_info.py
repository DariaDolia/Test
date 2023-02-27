import tables
import options

table_names = ['employees_info', 'countries']


def main():
    connection = tables.create_connection('employees.db')
    tables.create_table(connection, table_names, tables.table_descriptions)

    while True:
        options.options()
        try:
            option = int(input('\nChoose an option from list above: '))
            print()
        except ValueError:
            print('You entered invalid value. Try again')
            continue

        if option == 1:
            options.show_all_employees(connection)

        elif option == 2:
            name = input('enter a name: ').title().rstrip()
            while True:
                country_code = input('enter a country code UA, PL, UK: ').upper().strip()
                if country_code in ['UA', 'PL', 'UK', '']:
                    salary = float(input('enter a salary: ').replace(',', '.'))
                    options.create_new_employees(connection, name, country_code, salary)
                    break
                else:
                    print('\nYou enter incorrect country code. Try again')

        elif option == 3:
            name_of_employee = input('\nEnter a NAME of employee you wanna delete: ').title()
            options.delete_employee(connection, name_of_employee)

        elif option == 4:
            options.country_statistics(connection)

        elif option == 5:
            return


if __name__ == '__main__':
    main()
