import tables


def options():
    print()
    print('1. Show all employees')
    print('2. Create a new employees')
    print('3. Delete an employees')
    print('4. Country statistics')
    print('5. Exit')


def show_all_employees(connection_obj):
    cursor = connection_obj.cursor()
    cursor.execute("""select 
            e.name, coalesce(c.country, 'Unknown') country, e.salary 'salary ($)' 
            from employees_info e left join countries c
            on e.country_code = c.code""")

    data = cursor.fetchall()
    if not data:
        print('There are no data at the moment')
        return

    width1, width2, width3 = tables.width_of_columns(cursor, data)
    tables.column_names(cursor, name=width1, country=width2, salary=width3)

    for name, country, salary in data:
        print(f'{name:{width1}}|{country.center(width2)}|{salary:{width3},.2f}|')


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


def country_statistics(connection_obj):
    query_group_by_country = """select 
            coalesce(c.country, 'Unknown') country, count(*) num_employees, 
            sum(salary) 'total salary ($)', max(salary) 'max salary ($)'
            from employees_info e left join countries c 
            on e.country_code = c.code
            group by country;"""

    cursor = connection_obj.cursor()
    cursor.execute(query_group_by_country)
    data = cursor.fetchall()

    if not data:
        print('There are no data at the moment')
        return

    width1, width2, width3, width4 = tables.width_of_columns(cursor, data)
    tables.column_names(cursor, country=width1, name=width2, tot_salary=width3, max_salary=width4)

    for country, num_employees, tot_sal, max_sal in data:
        print(f'{country:{width1}}|{num_employees:{width2}}|{tot_sal:{width3},.2f}|{max_sal:{width4},.2f}|')
