# Book Reads 
## Deployed Live link 
* [BookReads](https://book-reads.herokuapp.com/) - https://book-reads.herokuapp.com/

* pic of responsive design 
* small paragraph introducing

----
## UX Design


### User Goals 

### Site Owner Goals

-------
## User Experience
### Target Audience
### User Requirements & Expectations
-----
## Structure
### Flowchart
### Current Features

#### Main Menu

#### Add Books

#### Display all Books

#### Delete Book

#### Exit

### Future Features I would like to add
1. Add a feature to calculate how long it took for the reader to complete a book.
2. Add an upload photo feature.
3. Add a Wishlist option on the menu and feature to add books you would like to add to your wishlist.
4. Calculate how many books you have read in the year.
5. Add books read in one year into a yearly worksheet. 

## Testing & Validation

### PEP8

## Bugs

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

## Acknowledgement 
### Special thanks to the following:
* Code Institute for providing this learning platform.
* Code Institute Student Support Team & Tutor Assistance for all your help. 
* Adegbenga Adeye, Code Institute Mentor for the valuable guidance and advice.
* CI Slack Community for assistance in any help or queries asked.





















