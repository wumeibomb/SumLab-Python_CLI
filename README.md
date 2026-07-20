# Python CLI Project!
 - This is a summative lab project done to showcase the ability to create a functional CLI. (please ignore folder models and file data/user_log.txt)

## To access:
 1) To use this CLI tool, clone this git repo onto your computer and ensure that you have python installed. For this CLI, pip install is not requried.
 2) Using your terminal on your preferred IDE, write \\
 python main.py \\. This will open up the help section for the CLI tool for your better understanding.
 3) The userdata input automatically goes into the data/main.json file which can be used for your own reference.
 - Now, you can easily use the CLI tool to create users, projects and tasks!

## Commands to know!
 - Main commands:
     - New - Adds a new user, takes username and email
     - Users - lists users within the database
     - add-project - Adds a project to the specified username
     - add-task - Adds a task to the project 
     
## Class Methods!:
 - class_User, this class is the parent class, seen to be inherited by the Project class. 
 - class_Project, this class is a child of the User class. Used to add projects to the user's profile
 - class_Tasks, this class is a child of Project. Adds tasks to specified projects. 
## Complications:
 - Testing not implemented 
 - doing add-projects and add-task before creating a user causes an error
 - Ran into an issue with trying to implement tabulate to the CLI.
 

