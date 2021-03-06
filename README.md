# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* Quick summary
* Python 3.7, Django 2.1
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

* Summary of set up
This build uses the django library with a MySQL database.
* Configuration
1. Install Python 3.7 from:
https://www.python.org/downloads/
- Make sure that python is download into a 'easy to access' directory.
2. Install Django library according to the instructions on: 
https://docs.djangoproject.com/en/2.1/topics/install/
3. Install MySQL Workbench

* Database configuration:
- Create an empty mySQL database named 'ifb299_db'
- Create a mySQL user for Django to use to connect and interact with the database
- In the project directory, run python manage.py migrate (this generates all tables necessary for the webapp)
- via the mySQL workbench 'data import wizard' use the CSV files in the git repository to populate the search_car, search_store, search_customer and search_order   tables.
- Run the server!

* How to run tests
To run the website run the below command in command prompt(or similar)
'python manage.py runserver'
Make sure that you are in the directory containing the manage.py file in the command line.
* Deployment instructions


### Contribution guidelines ###

* Completed tasks
1. Create Homepage with navbar and image (Homepage) by Margat
2. Create ERD (Database) by Conorbros
3. Create tables for (Database) by Ethra
* Writing tests

* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact


### Following tasks for Sprint 1 ###

* Set-up home page (Done)
* Create database
* Create ERD
* Find a way to get information to a suitable format in Django
