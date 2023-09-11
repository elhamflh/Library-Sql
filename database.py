import sqlite3
import datetime

connection= sqlite3.connect('Library-data.db')

CREATE_TABLE_BOOK = """
CREATE TABLE IF NOT EXISTS book (
book_id INTEGER PRIMARY KEY,
title TEXT,
writer TEXT,
getting_date INTEGER,
delivery_date DEFAULT DATETIME,
FOREIGN KEY (getting_date) REFERENCES book(book_id)
);
"""

CREATE_TRIGGER_BOOK = """
CREATE TRIGGER IF NOT EXISTS set_default_delivery_date
AFTER INSERT ON book
BEGIN
  UPDATE book
  SET delivery_date = datetime(getting_date, '+2 weeks')
  WHERE rowid = NEW.rowid;
END;
"""

CREATE_TABLE_USERS="""
CREATE TABLE IF NOT EXISTS users (
user_id INTEGER ,
username TEXT,
number INTEGER,
age INTEGER,
FOREIGN KEY (user_id) REFERENCES book(book_id));
"""

INSERT_BOOKS="""INSERT INTO book VALUES(?,?,?);"""
INSERT_USER= """INSERT INTO users VALUES (?,?,?);"""
SELECT_ALL_BOOKS='''SELECT * FROM book;'''
SELECT_NEW_BOOK = """
SELECT book.* FROM book
JOIN users ON users.user_id = book.book_id
WHERE delivery_date > ? AND AND user.username = ? ;
"""

SELECT_READ_BOOK = """
SELECT book.* FROM book
JOIN users ON users.user_id = book.book_id
WHERE delivery_date < ? AND user.username = ? ;
"""
SEARCH_BOOK ="""SELECT BOOK.* FROM book WHERE  title LIKE"""





def create_table():
    with connection:
        connection.execute(CREATE_TABLE_BOOK)
        connection.execute(CREATE_TABLE_USERS)
        connection.execute(CREATE_TRIGGER_BOOK)


def add_book(title, writer, getting_date):
    with connection:
        connection.execute(INSERT_BOOKS, (title, writer, getting_date))
         # Commit the changes

def add_user(username, number, age):
    with connection:
        connection.execute(INSERT_USER, (username, number, age))
         # Commit the changes

def all_books():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_ALL_BOOKS)
        return cursor.fetchall()

def now_books(username):
    with connection:
        cursor = connection.cursor(username)
        today_timestamp = datetime.datetime.today().timestamp()
        cursor.execute(SELECT_NEW_BOOK, (today_timestamp,username,))
        return cursor.fetchall()

def read_book(username):
    with connection:
        cursor = connection.cursor()
        today_timestamp = datetime.datetime.today().timestamp()
        cursor.execute(SELECT_READ_BOOK, (today_timestamp,username,))
        return cursor.fetchall()
       

def search_book(search_terms):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SEARCH_BOOK, (f"%{search_terms}%",))
        return cursor.fetchall()