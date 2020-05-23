# Cominder
## DTC - Team 14 - Team Four Ten(s)
##### Jun Yeon (T2), Choi Song (T2), Jessica Hong (T1), and Duncan Keen (T1)

>
>
**Warning, you must have Python 3.x installed in order to follow any of these steps.
[Click here](https://www.python.org/downloads/) to download Python.**

## How is the Repository Organized?

Django revolves around applications, where each application is in charge of each feature of our web-application 
(task_tracker, forums fridge, etc). You can see the full list of our application in the `Apps` directory in the root. 
When starting a new application, each directory automatically generates a `urls.py` (contains all the paths to all 
pages), `admin.py` (allows you to register Models (tables in MySQL) in the admin GUI, and `views.py` (renders HTML 
pages or generic classes on a page). 

## To Assemble a Development Environment
>1. Make a directory in your local system where you wish to pull the project from the remote repository.
>
>2. In your terminal/command line<cmd>, navigate to the directory you just created.
>
>3. `git init`  to initialize git
>
>4. `git clone https://github.com/cysong12/COMP-2800-Team-DTC-14-Cominder.git` to copy remote repository from github

Mac/Linux:
>5. If you do not have Python 3.x installed, go to https://docs.brew.sh/Homebrew-and-Python and follow the instructions
>
>6. `source our_env/bin/activate` to activate virtual environment so that you don’t download dependencies separately
>
>7. `python3 manage.py makemigrations`    to migrate database 
>
>8. `python3 manage.py migrate`        to migrate database
>
>9. `python3 manage.py loaddata Apps/fixtures/categories`        to preload data for categories table
>
>10. `python3 manage.py loaddata Apps/fixtures/subforums`               to preload data for sub-forums table
>
>11. `python3 manage.py runserver`                     to run the server on local host on http://127.0.0.1:8000/
>

Windows:
>5. If you haven't already, install Python 3.x [here](https://www.python.org/downloads/)
>
>6. `.\our_env\bin\activate` to activate the virtual environment.
>
>7. `python manage.py makemigrations`    to migrate database 
>
>8. `python manage.py migrate`        to migrate database
>
>9. `python manage.py loaddata Apps/fixtures/categories`        to preload data for categories table
>
>10. `python manage.py loaddata Apps/fixtures/subforums`               to preload data for sub-forums table
>
>11. `python manage.py runserver`                     to run the server on local host on http://127.0.0.1:8000/

## To access Forums

You must update your profile with Preference settings in order to view forums with that category. For example, in order
to view Sports Forum posts, you must update your profile preferences to `Sports`.

## To login with Google/Facebook

Due to the short time frame we were given to complete this assignment, we could not come up with a script to allow social logins to <br>
work on local host. If you would like to access our social logins, please navigate to our hosted website http://cominder.herokuapp.com/ . We apologize for the inconvenience.

## To create an Admin User and access Detailed Configurations.
>1.) Navigate to the project directory `Cominder` on terminal <br/>
>
>2.) Type in `python manage.py createsuperuser`. Then, it will prompt you to create an account. Create the account. <br>
>
>3.) The account you have just made has admin privileges. Run the localhost server (`python manage.py runserver`) and 
navigate to `localhost:8000/admin` <br>
>
>4.) Log in with the account you have just created. Once you are logged in, you should be able to view all objects and 
>users on the website.
>
Note: With the admin account, you will be able to access all configurations. No passwords or keys are needed.

## Test Plan Link Below

https://docs.google.com/spreadsheets/d/1GZHuXnIMMpEJd1Im2Sq9-rc1fpq_l0HCYTv1ln_H0Ng/edit?usp=sharing
