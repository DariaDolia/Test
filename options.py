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

    d = {key: value for key, value in zip(('name', 'country', 'salary'), tables.width_of_columns(cursor, data))}

    for name, country, salary in data:
        print(f'{name:{d["name"]}}|{country.center(d["country"])}|{salary:{d["salary"]},.2f}|')


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

    d = {key: value for key, value in zip(('country', 'num', 'tot_salary', 'max_salary'),
                                          tables.width_of_columns(cursor, data))}

    for country, num_employees, tot_sal, max_sal in data:
        print(f'{country:{d["country"]}}|{num_employees:{d["num"]}}|{tot_sal:{d["tot_salary"]},.2f}|'
              f'{max_sal:{d["max_salary"]},.2f}|')
