
import tables
import options


# WIDTH_NAME_COL = 20
# WIDTH_COUNTRY_COL = 20
# WIDTH_SALARY_COL = 20
# FULL_WIDTH = WIDTH_NAME_COL + WIDTH_COUNTRY_COL + WIDTH_SALARY_COL + 3


create_employees_info = """create table employees_info(
    name text not null,
    country_code text,
    salary integer not null);"""

create_countries = """create table countries (
        code text not null,
        country text not null);"""


def main():
    connection = tables.create_connection('employees.db')

    if tables.check_if_table_exists(connection, 'employees_info') is False:
        tables.create_table(connection, create_employees_info)

    if tables.check_if_table_exists(connection, 'countries') is False:
        tables.create_table(connection, create_countries)
        tables.data_for_countries_table(connection)

    while True:
        options.options()
        try:
            option = int(input('\nChoose an option from list above: '))
            print()
        except ValueError:
            print('You entered invalid value. Try again')
            continue

        if option == 1:
            options.show_all_employees(connection, width_name=20, width_country=20, width_salary=20)

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
            options.country_statistics(connection, width_country=20, width_name=15, width_salary=20)

        elif option == 5:
            return


main()
