import psycopg2
import contextlib

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

@contextlib.contextmanager
def dbconnection_manager(dbname):
    """
    Context manager to handle database connection
    param dbname: name of database
    """
    connection_state = False
    try:
        conn =  psycopg2.connect(f"host = localhost, user=postgres dbname={dbname}")
        connection_state = True

        print(f'connected to {dbname}...')
        cur = conn.cursor()
        conn.set_session(autocommit=True)
        print('session set to autocommit')
        yield (cur, conn)

    except psycopg2.Error as e:
        raise

    finally:
        if connection_state:
            print('closing cursors and connections')
            cur.close()
            conn.close()
        else:
            print('no connection made to the database')