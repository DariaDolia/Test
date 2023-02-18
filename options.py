import tables


def options():
    print()
    print('1. Show all employees')
    print('2. Create a new employees')
    print('3. Delete an employees')
    print('4. Country statistics')
    print('5. Exit')


def show_all_employees(connection_obj, width_name, width_country, width_salary):
    cursor = connection_obj.cursor()
    cursor.execute("""select 
            e.name, coalesce(c.country, 'Unknown') country, e.salary 'salary ($)' 
            from employees_info e left join countries c
            on e.country_code = c.code""")

    tables.column_names(cursor, name=width_name, country=width_country, salary=width_salary)

    for name, country, salary in cursor.fetchall():
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


def country_statistics(connection_obj, width_country, width_name, width_salary):
    query_group_by_country = """select 
            coalesce(c.country, 'Unknown') country, count(*) num_employees, 
            sum(salary) 'tot_salary ($)', max(salary) 'max_salary ($)'
            from employees_info e left join countries c 
            on e.country_code = c.code
            group by country;"""

    cursor = connection_obj.cursor()
    cursor.execute(query_group_by_country)

    tables.column_names(cursor, country=width_country, name=width_name,
                        tot_salary=width_salary, max_salary=width_salary)

    for country, num_employees, tot_sal, max_sal in cursor:
        print(f'{country:{width_country}}|{num_employees:{width_name}}|'
              f'{tot_sal:{width_salary},.2f}|{max_sal:{width_salary},.2f}|')
