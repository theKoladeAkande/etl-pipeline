""" Creates tables """
import psycopg2
import contextlib
import sql_queries

def psycopg2_error_handler(fn):
    """Function decorator for handling psycopg2 errors"""
    def inner(*args, **kwargs):
        try:
            fn(*args, **kwargs)
        except psycopg2.Error as e:
            print(e)
            raise
    return inner

@psycopg2_error_handler
def data_defination(query: str, cursor, execute_many=False, data=None):
    """ Executes query to create table"""
    if execute_many:
        cursor.executemany(query, data)
    else:
        cursor.execute(query)

    if "DROP" in query:
        print('Table droped  succesfuly')
    elif "CREATE" in query:
        print("Table created successfuly")

@contextlib.contextmanager
def dbconnection_manager(dbname):
    """ Context manager to handle database connection"""
    connection_state = False
    try:
        conn =  psycopg2.connect(f"host = localhost, user=postgres dbname={dbname}")
        connection_state = True

        print(f'connected to {dbname}...')
        cur = conn.cursor()
        conn.set_session(autocommit=True)
        print('session set to autocommit')
        yield cur

    except psycopg2.Error as e:
        raise

    finally:
        if connection_state:
            print('closing cursors and connections')
            cur.close()
            conn.close()
        else:
            print('no connection made to the database')

@psycopg2_error_handler
def create_db(cursor, dbname):
    cursor.execute(f"DROP DATABASE IF EXISTS {dbname}")
    cursor.execute(f"CREATE DATABASE {dbname} WITH ENCODING 'utf8' TEMPLATE template0")


if __name__ == "__main__":
    with dbconnection_manager(dbname='practice') as cursor:
        create_db(cursor, "sparkifydb")

    with dbconnection_manager(dbname="sparkifydb") as cursor:
        for query in sql_queries.DROP_QUERYS:
            try:
                data_defination(query, cursor)
            except psycopg2.Error as e:
                print(e)
    with dbconnection_manager(dbname="sparkifydb") as cursor:
        for query in sql_queries.CREATE_QUERYS:
            data_defination(query, cursor)