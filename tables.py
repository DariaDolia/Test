import sqlite3


def create_connection(db_name):
    with sqlite3.connect(db_name) as connection:
        return connection


def create_table(connection_object, table):
    cursor = connection_object.cursor()
    cursor.execute(table)


def check_if_table_exists(connection_obj, table):
    cursor = connection_obj.cursor()
    cursor.execute("""SELECT count(name) FROM sqlite_master WHERE type='table' AND name=?""", [table])
    if cursor.fetchone()[0] == 1:
        return True
    return False


def data_for_countries_table(connection_obj):
    data = [
        ('UA', 'Ukraine'),
        ('PL', 'Poland'),
        ('UK', 'United Kingdom'),
    ]

    cursor = connection_obj.cursor()
    cursor.executemany(""" insert into countries values (?, ?)""", data)
    connection_obj.commit()
