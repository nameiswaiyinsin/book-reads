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
RECORDS = SHEET.worksheet('records')

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
        print("\nDate is recorded in 'DD/MM/YYYY' format.")
        start_date = input("Enter the start date: ")
        end_date = input("Enter the end date: ")
        if validate_date(start_date, end_date):
            book_details.append(start_date)
            book_details.append(end_date)
            break
    while True:
        print("\n0 on the rating system is Bad and 5 is Excellent.")
        rating = input("Enter rating for the book out of 5: ")
        if validate_rating(rating):
            book_details.append(rating)
            break
    while True:
        review = input("\nEnter review notes: ")
        if validate_data(review):
            book_details.append(review)
            break
    return update_records_worksheet(book_details)

    
def validate_data(values):
    """
    Validate to check if the string inputs have data.
    """
    try:
        if len(values) == 0:
            raise ValueError()
    except ValueError:
        print("Empty string, please input data. \n")
        return False
    return True


def validate_date(start_date, end_date):
    """
    Validate the start and end date to check if it is in the right format of dd/mm/yyyy 
    """
    try:
        if datetime.datetime.strptime(start_date, '%d/%m/%Y') is False:
            raise ValueError()
        elif datetime.datetime.strptime(end_date, '%d/%m/%Y') is False:
            raise ValueError()
        try:
            if datetime.datetime.strptime(start_date, '%d/%m/%Y') > datetime.datetime.strptime(end_date, '%d/%m/%Y'):
                raise ValueError()
        except ValueError:
            print("Error: Start date is later than your end date. \n"
                  "Input start and end date again. \n")
            return False
    except ValueError:
        print("Incorrect date format, should be 'DD/MM/YYYY'. \n")
        return False
    return True


def validate_rating(rating):
    """
    Validate the rating to check if it a number, from 0-5"
    """
    try:
        if rating == int(rating):
            raise ValueError()
    except ValueError:
            print("\nIncorrect string input. \n"
            "Please input a number rating between 0-5. \n")
            return False
    try:
        if int(rating) > 5:
            raise ValueError()
        elif int(rating) < 0:
            raise ValueError()
    except ValueError:
            print("\nIncorrect number range input. \n"
            "Please input a rating between 0-5. \n")
            return False
    return True


def update_records_worksheet(record):
    """
    Update records worksheet, adding a new row when new book is added.
    """
    print("\nUpdating Book Diary...\n")
    records_worksheet = SHEET.worksheet("records")
    records_worksheet.append_row(record)
    print("Book diary updated successfully!\n")


def display_all_books():
    """
    This function retrieves all the books recorded from the Google sheet and displays them in the terminal.
    """
    all_records = RECORDS.get_all_records()
    if all_records:
        for records in all_records:
            print_all_books(records)
    else:
        print("\nNo books recorded in book diary yet!")

def print_all_books(existing):
    """
    Display all the books.
    """
    book = []
    print("-----")
    for key, value in existing.items():
        print(f"{key}: {value}")
    print("-----")
    return book


def delete_book():
    """
    Delete a book from Google spreadsheet.
    """
    while True:
        name = input("Please enter book name. \n"
                     "Or type 'exit' too return to main menu.: ")
        book = RECORDS.col_values(1)
        if name == "exit":
            menu()
        if name in book:
            rownum = book.index(name) + 1
            row = RECORDS.row_values(rownum)
            headings = RECORDS.row_values(1)
            search = dict(zip(headings,row))
            for key, value in search.items():
                print(f"{key}: {value}")
            print("\nDeleting book from Book Diary...\n")
            RECORDS.delete_rows(rownum)
            print("Book has been deleted! \n")
            break
        else: 
            print("Error: No book with that title. \n"
                  "Please enter valid title.\n")

menu()
