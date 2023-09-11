import sqlite3
import datetime
import database

home="""
---welcome to online library--
how can i help you?

1)add book.
2)add user.
3)all of your library.
4)reading now.
5)book history.
6)search a book.
7)exit.


selection:"""
welcome="Hi there!"

print(welcome)
database.create_table()


def app_add_books():
    title = input("enter the book's title: ")
    writer = input("enter the writer's name: ")
    getting_date = input('add getting date (dd/mm/YYYY ): ')
    parsed_date = datetime.datetime.strptime(getting_date, "%d/%m/%Y")
    timestamp = parsed_date.timestamp()

    database.add_book(title, writer, timestamp) 
    
def app_add_user():
    username= input("enter your username: ")
    number=input("add your number: ")
    age=input ("enter your age: ")
    
    database.add_user(username, number, age)

def app_all_books(book):
    print('---All Books--')
    for b in book:
        getting_date = datetime.datetime.fromtimestamp(b[3])
        human_date = getting_date.strftime('%d/%b/%y')
        print(f"{b[1]}: {b[2]} (on {human_date})")
    print("----\n")

def app_reading_new_book():
    username= input("pls enter your username: ")
    book= database.SELECT_NEW_BOOK(username)
    if book:
        app_all_books('New books:',book)
    else:
        print("THERE ISN'T ANY NEW BOOK.")

def app_old_book():
    username= input("please enter your username: ")
    book= database.SELECT_NEW_BOOK(username)
    if book:
        app_all_books('books history:',book)
    else:
        print("THERE ISN'T ANY NEW BOOK.")

def search_book():
    search_term= input("enter the books title:")
    books = database.search_book(search_term)
    if books:
        app_all_books(books)
    else:
        print("CANT FIND...")



while (user_input := input(home)) !="7":
    if user_input == "1":
        app_add_books()
    elif user_input == "2":
        app_add_user()
    elif user_input == "3":
        app_all_books()
    elif user_input == "4":
        app_reading_new_book()
    elif user_input == "5":
        app_old_book()
    elif user_input == "6":
        search_book()
    else:
        print("invalid entery.pls try again.")
 


