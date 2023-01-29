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
print("Welcome to your Book Reads Record diary. \n")

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
