'''
    This is a program to make predictions for the prices of cars.
    I use various models to make predictions and gauge the accuracy of each
    Tools: Random Forest, Gradient Boosting, SARIMA, ARIMA,
'''

import mysql.connector
from mysql.connector import Error

def create_connection():
    ''' create a database connection to mySQL database '''
    conn = None
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='owura',
            password='owura@sql123',
            database='library_management'
        )
        if conn.is_connected():
            print('successfully connected with database')

    except Error as e:
        print(f'Error: {e}')

    return conn


def get_books():
    '''Fetch all books from the Books table'''
    connection = create_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Books")
        books = cursor.fetchall()

        print("Books in the library:")
        for book in books:
            print(book)

        cursor.close()
    except Error as e:
        print(f"Error: '{e}'")
    finally:
        if connection.is_connected():
            connection.close()
            print("Database connection closed")


if __name__ == "__main__":
    get_books()