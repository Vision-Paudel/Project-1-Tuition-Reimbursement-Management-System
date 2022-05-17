from typing import Optional, Any

import psycopg2
from psycopg2._psycopg import OperationalError


def create_connection():
    try:
        conn = psycopg2.connect(
            # Information removed for security purposes.
            database='mydb',
            user='',
            password='',
            host='',
            port=''
        )
        return conn
    except OperationalError as e:
        print(f"{e}")
        return None


def close_connection(connectionToClose: Optional[Any]):
    connectionToClose.close()


connection = create_connection()


def _test():
    print(connection)
    close_connection(connection)


if __name__ == "__main__":
    _test()
