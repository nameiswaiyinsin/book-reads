# Book Reads 
Welcome to [BookReads](https://book-reads.herokuapp.com/) README.md file!

![](/assets/images/responsive%20design.png)
BookReads is a Book Diary programme to record all the books you have read, hence it is called BookReads! 

This programme allows the users to input / record the books that they have read. The book diary allows the user to input the title of the book, the author, what date they started reading the book and what date they completed the book, a rating out of 5 and a brief review. 

The programme also allows the user to display all their inputted books to get a look at see how many books, type of book and review at a glance. 

The user can also delete a book if they have inserted mistake inputs.

## Deployed Live link 
* [BookReads](https://book-reads.herokuapp.com/) URL - https://book-reads.herokuapp.com/


----
## UX Design & Expectations
### User Goals 
As a user, I want:

* Understand the purpose of the programme on loading
* Navigate through the interface smoothly with clear instructions
* A programme with a simple menu
* A programme with good feedback on my inputs and processing of my information
* To be able to easily add books
* To be able to view all my books at a glance and delete books

### Site Owner Goals
As the owner of this programme, my goals are to:

* Create a programme that is easy to use and navigate
* Create a programme with clear instructions for the user
* Create a programme that can add books
* Create a programme that can display all books
* Create a programme that can delete book
* Create a programme that successfully interacts with Google Sheets

-----
## Structure
### Flowchart 
![](/assets/images/flowchart.jpeg)

### Current Features
#### 1. Main Menu
The main menu starts with a welcome message: "Welcome to your Book Reads Record diary!". The menu gives the user 4 options to choose from. The user is asked to choose options from 1 - 4, inputting the number of the option they would like to proceed with.

![](/assets/images/mainmenu.png)

#### 2. Add Books
This menu option allows the user to add their books they would like to record. The user is invited to add the book title, author, start date, end date, a rating out of 5 and a review note. Once they input the details and the different sections of the details inputted are validated with the correct input data, the book details are added to the google spreadsheet.
![](/assets/images/addbookpt1.png)
![](/assets/images/addbookpt2.png)

#### 3. Display all Books
This menu option allows the user to display all their book entries that are validated and stored in the database.

![](/assets/images/displaybook.png)

#### 4. Delete Book
This menu option allows the user to delete a book entry from the database by asking them to input the title of the book and then deleting the corresponding book details.
![](/assets/images/deletebook.png)

#### 5. Exit
This menu option allows the user to exit from the programme, displaying a thank you and a goodbye message.

![](/assets/images/exitprogram.png)

### Future Features I would like to add
* Add a feature to calculate how long it took for the reader to complete a book.
* Add an upload photo feature.
* Add a Wishlist option on the menu and feature to add books you would like to add to your wishlist.
* Calculate how many books you have read in the year.
* Add books read in one year into a yearly worksheet. 


## Testing & Validation
### 1. Easy Navigation and Clear Instructions

I tested the programme at each stage to ensure that the program was working correctly and that the instructions given were clear to make the experience more accessible for the user. I tested the navigation by going through the menu options which gave me clear information on what to do and the exact type of data input I required.

I also tested the program by entering wrong information and challenged the input data types such as strings, integers and numbers within a specific range of 0-5. 

By entering the wrong information, I can test whether my error messages are showing and giving clear instructions to the users where they can input their data again. 

### 2. Validate strings

I validated the string to ensure that input entered by the user is accepted in the Title, Author and Review section of the Add Book option.

![](/assets/images/validating%20string.png)
 
The diary updates successfully when the data inputted is validated correctly. 

![](/assets/images/validate%20string%20and%20successful.png)


### 3. Validate date
I tested whether the date is validated correctly by entering a wrong format such as an outlandish date of 45 that does not exist. It must be an actual date for the date data to be accepted. 

I also tested the date validation to ensure that the start date is never later than the end date. 

![](/assets/images/validating%20date.png)

### 4. Validate integer and range
I tested the rating section by ensuring that only integers could be accepted in this section and if the inputted value is not an integer, an error message would appear as "Incorrect string input." and prompting the user to insert a number rating between 0-5.

![](/assets/images/validate%20rating%20integer.png)

I also tested to ensure that only a number within the range of 0-5 would be accepted. If the inputted number is outside the range of 0-5, an error message would appear as: "Incorrect number range input." and would again prompt the user to insert a number between 0-5.

![](/assets/images/validate%20rating%20range.png)

### 5. Testing Display Book 
When the menu option2 Display Book is selected, it will display all the current books that have been added.

![](/assets/images/display%20all%20books.png)

After some books have been deleted, the Display Book option will reflect this and display the books that have not been deleted.

![](/assets/images/display%20book%20after%20delete.png)

When there is no books recorded, or if all the books have been deleted, "No books recorded in diary yet!" will be printed to the terminal for the user.

![](/assets//images/no%20books%20to%20display.png)

### 6. Testing Delete Book
I tested this menu option by ensuring that the input data would match the command, and in this case if the user wanted to exit, they could also type "exit" into the interface, otherwise they would receive an error message displaying "No book with that title. Please enter valid title." and they would be prompted again to type in the book title or "exit" to exit back to the main menu.

![](/assets/images/delete%20book%20or%20exit.png)

When the correct book title is inserted, the book will be deleted from the database and the user would be informed. 

![](/assets/images/delete%20book%20successful.png)

### 7. Successful interaction with Google Sheets
I tested whether the programme is successfully interacting with Google sheet by checking if the sheet would update when a new book was added and/or when a book was deleted when the relevant menu option was chosen, and it was successful. 

### 8. PEP8
I used the PEP8 validator tool in Gitpod workspace and there was no problem detected. 

#### How to install PEP8 validator tool on Gitpod workspace:
1. Type `pip3 install pycodestyle` in the gitpod workspace terminal.
2. Type CMD+SHIFT+P on MAC or CTRL+SHIFT+P on Windows.
3. Type `linter` into search box that pops up.
4. Click on "Python: Select Linter".
5. Then select, "pycodestyle" 

PEP8 error will now be underlined in red and listed on "**Problems**" tab beside your terminal.

## Bugs
* Validating the rating system - I was trying to validate and integer and a range of numbers by nesting the conditions within a loop of code: a try - if - elif - except in within a try - if - except, which kept displaying an error. I fixed it by taking out of the nested code. 

## Deployment
The live deployment can be found using the following URL - https://book-reads.herokuapp.com/

### Heroku
[Heroku Official Page](https://devcenter.heroku.com/articles/git)

1. Log in to your account at heroku.com.
2. Create a new app, add a unique app name and choose your region.
3. Click on create app.
4. Go to "**Settings**" tab.
5. Under Config Vars store any sensitive data in .json file. Name 'Key' field `'CREDS'`, and copy the content of the creds.json file & paste it to the 'Value' field. 
6. Under Config Vars, add another key `'PORT'` and value `'8000'`.
7. Add required buildpacks. For this project, I set up 'Python' and 'node.js' in that order.
8. Scroll up and go to "**Deploy**" tabs and select "GitHub" in "Deployment method"
9. To link up the Heroku app to our Github repository code enter your repository name, click 'Search' and then 'Connect' when it shows below.
10. Choose the branch you want to buid your app from. - I chose "Deploy Branch" which requires me to manually deploy again in the future if I make any changes to the repository.

    If prefered, click on "Enable Automatic Deploys", which keeps the app up to date with your GitHub repository.
11. Wait for the app to build. Once ready you will see the “App was successfully deployed” message and a 'View' button to take you to your deployed link.


### Fork Repository
To fork the repository by following these steps:

1. Go to the GitHub repository
2. Click on Fork button in upper right hand corner

### Clone Repository
You can clone the repository by following these steps:

1. Go to the GitHub repository
2. Locate the Code button above the list of files and click it
3. Select if you prefer to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY) 
7. Press Enter to create your local clone.

## Technologies used
### Language
* Python

### Framework & Tools
* Lucidchart
* Gitpod
* Github
* Google Cloud Platform
* Heroku

### Libraries
#### Python Library
* [Datetime](https://docs.python.org/3/library/datetime.html)

#### Third Party Libraries
* [Gspread](https://docs.gspread.org/en/v5.3.2/) 
* [Google Auth](https://google-auth.readthedocs.io/en/master/)


## Credits

* [Creating a menu](https://stackoverflow.com/questions/19964603/creating-a-menu-in-python)
* [How to Check If a String Is an Integer](https://youtu.be/5W2EESdJQ5I)
* [How to Validate a Date Using Python](https://youtu.be/5n_JagFqWeg)
* [How to append values](https://stackoverflow.com/questions/48234473/python-attributeerror-dict-object-has-no-attribute-append)


## Acknowledgement 
### Special thanks to the following:
* Code Institute for providing this learning platform.
* Code Institute Student Support Team & Tutor Assistance for all your help. 
* Adegbenga Adeye, Code Institute Mentor for the valuable guidance and advice.
* CI Slack Community for assistance in any help or queries asked.





















