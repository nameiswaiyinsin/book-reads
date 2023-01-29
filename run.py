import datetime
import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('book_reads')

records = SHEET.worksheet('records')

def menu():
    """
    Display a menu with a list of options to choose from
    """
    print("Welcome to your Book Reads Record diary! \n")

    while True:
        print("""
            -----Menu-----
            1. Add Book
            2. Display All Books 
            3. Delete Book
            4. Exit
            """)

        option = input("Please select options from 1-4: ")
        if option == '1':
            add_book()
        elif option == '2':
            display_all_books()
        elif option == '3':
            delete_book()
        elif option == '4':
            exit_programme()
        else:
            print("Invalid option, please select number from 1-4: ")


def add_book():
    """
    Add a new book to the google spreadsheet with the accompanying information
    Book Title, Author, Start Date, End Date, Rating, Review
    """
    
    book_details = []
    while True:
        book_title = input("Please enter the book title: ")
        if validate_data(book_title):
            book_details.append(book_title)
            break
    while True:
        author = input("Please enter the author: ")
        if validate_data(author):
            book_details.append(author)
            break
    while True:
        print("\nDate is recorded in 'DD-MM-YYYY' format.")
        start_date = input("Enter the start date: ")
        end_date = input("Enter the end date: ")
        if validate_date(start_date, end_date):
            book_details.append(start_date)
            book_details.append(end_date)
            break
    while True:
        print("\n1 on the rating system is Bad and 5 on rating system is Excellent.")
        rating = input("Enter rating for the book out of 5: ")
        if validate_rating(rating):
            book_details.append(rating)
            break
    while True:
        review = input("\nEnter review notes: ")
        if validate_data(review):
            book_details.append(review)
            break

    
def validate_data(values):
    """
    Validate to check if the string inputs have data.
    """


def validate_date(start_date, end_date):
    """
    Validate the start and end date to check if it is in the right format of dd/mm/yyyy
    """


def validate_rating(rating):
    """
    Validate the rating to check if it a number, from 0-5"
    """




menu()
