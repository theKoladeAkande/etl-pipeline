import contextlib

import psycopg2
from connection_manger import dbconnection_manager
import sql_queries

def psycopg2_error_handler(fn):
    """Function decorator for handling psycopg2 errors
       :fn: a function that executes postgresql queries
    """
    def inner(*args, **kwargs):
        try:
            fn(*args, **kwargs)
        except psycopg2.Error as e:
            print(e)
            raise
    return inner

@psycopg2_error_handler
def data_definition(query: str, cursor, execute_many=False, data=None):
    """
    Executes query to create or drop table
    :param query: string containing query
    :param cursor: cursor to the database
    :param execute_many: option for multiple queries execution
    :data: An iterable(preferably a list) of all data
    """
    if execute_many:
        cursor.executemany(query, data)
    else:
        cursor.execute(query)

    if "DROP" in query:
        print('Table dropped  succesfuly')
    elif "CREATE" in query:
        print("Table created successfuly")


@psycopg2_error_handler
def create_db(cursor, dbname):
    """
    Creates or drop database
    :param cursor: cursor connection to the database
    :param dbname: database name
    """
    cursor.execute(f"DROP DATABASE IF EXISTS {dbname}")
    cursor.execute(f"CREATE DATABASE {dbname} WITH ENCODING 'utf8' TEMPLATE template0")


if __name__ == "__main__":
    with dbconnection_manager(dbname='practice') as (cursor,conn):
        create_db(cursor, "sparkifydb")

    with dbconnection_manager(dbname="sparkifydb") as (cursor, conn):
        for query in sql_queries.DROP_QUERIES:
                data_definition(query, cursor)

    with dbconnection_manager(dbname="sparkifydb") as (cursor, conn):
        for query in sql_queries.CREATE_QUERIES:
            data_definition(query, cursor)