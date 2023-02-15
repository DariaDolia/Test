
def options():
    print()
    print('1. Show all employees')
    print('2. Create a new employees')
    print('3. Delete an employees')
    print('4. Country statistics')
    print('5. Exit')


def show_all_employees(connection_obj, width_name, width_country, width_salary, full_width):

    cursor = connection_obj.cursor()
    cursor.execute("""select e.name, c.country, e.salary 'salary ($)' 
        from employees_info e left join countries c
        on e.country_code = c.code""")

    col_names = [cn[0] for cn in cursor.description]

    print(f'\n{col_names[0].center(width_name)}|{col_names[1].center(width_country)}|'
          f'{col_names[2].center(width_salary)}|')
    print('-' * full_width)

    for name, country, salary in cursor.fetchall():
        if country is None:
            country = ''
        print(f'{name:{width_name}}|{country.center(width_country)}|{salary:{width_salary},.2f}|')


def create_new_employees(connection_obj, name, country_code, salary):
    cursor = connection_obj.cursor()
    cursor.execute("""insert into employees_info values (?, ?, ?)""", [name, country_code, salary])
    connection_obj.commit()


def delete_employee(connection_obj, name_of_employee):
    cursor = connection_obj.cursor()
    cursor.execute('delete from employees_info where name=?', [name_of_employee])
    if cursor.rowcount:
        connection_obj.commit()
        return
    print('There is not such name in the table')


def country_statistics(connection_obj, width_country):
    query_group_by_country = """select (select c.country from countries c where e.country_code = c.code) country, 
        count(*) num_of_employees, 
        sum(salary) tot_salary, max(salary) max_salary 
        from employees_info e
        group by country;"""

    cursor = connection_obj.cursor()
    cursor.execute(query_group_by_country)

    col_names = [cn[0] for cn in cursor.description]

    print(f'{col_names[0].center(width_country)}|{col_names[1].center(len(col_names[1])+2)}|'
          f'{col_names[2].center(len(col_names[2])+5)}|{col_names[3].center(len(col_names[3])+5)}')

    print('-' * (width_country + len(col_names[1]) + len(col_names[2]) + len(col_names[3]) + 15))

    for country, num_employees, tot_sal, max_sal in cursor:
        if country is None:
            country = ''
        print(f'{country:{width_country}}|{num_employees:{len(col_names[1]) + 2}}|'
              f'{tot_sal:{len(col_names[2])+5},.2f}|{max_sal:{len(col_names[3])+5},.2f}')
