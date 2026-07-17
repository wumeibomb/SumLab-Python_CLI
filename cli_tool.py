import argparse
from models import class_Tasks
from models import class_Project


#create users, projects and tasks
#display and search for projects
#structure commands logically with clear naming conventions and grouping.
#Use descriptive help text for every command and argument.
#Validate all user input to prevent incorrect usage or runtime errors.
#Offer default values and optional flags to increase flexibility.
#Handle exceptions with meaningful error messages, not cryptic stack traces.
#Avoid overwhelming the user—display only relevant info, and provide examples where helpful.

class User:
    user_list = []

    def __init__(self, user, email):
        self.user = user
        self.email = email
        self._projects = [] #testing
        User.user_list.append(self)

    @property
    def projects(self):
        return self._projects
    
    @projects.setter
    def project(self, value):
        if not isinstance(value, User):
            raise TypeError("Must be of the USER class")
        self._projects = value

    def add_user(self, user):
         self.user_list.append(user)
         print(user_list)

User("flop231", "flop@gmial.com")

def add_user(args):
        user = user_list.get(args.USER)
        user_list[args.USER] = user
        email = email_list.get(args.EMAIL)
        email_list[args.EMAIL] = email
        print(f"Added user {args.USER}")
        print(user_list,email_list)
    
def manage_users(args):
        users = user_list.get(args.list)
        user_list[args.list] = users
        
        print(users)

email_list = {}
user_list = {}

def manage_projects(args):
     print(f"{args.username} added {args.title}")

def add_manage_tasks(args):
    task = class_Tasks(args.pro)
    task.add_manage_tasks(task)

def main():

    parser = argparse.ArgumentParser(description= "Python Project Management CLI tool.")
# options: create user, manage users(display the users) and select them, display projects - assign task to projects and mark complete.
#if certain user selected, open this set of projects. don't show the others.
    subparsers = parser.add_subparsers()
    add_parser = subparsers.add_parser("New", help="Add a new USER!") #new user, no list of users
    add_parser.add_argument("USER", help="Name of the USER!") #what you write after New
    add_parser.add_argument("EMAIL", help="Email of the New User")
    add_parser.set_defaults(func=add_user)
    
    manageuser_parser = subparsers.add_parser("Users", help="Lists users")
    manageuser_parser.add_argument("list", help="list the users")
    manageuser_parser.set_defaults(func=manage_users)

    managetasks_parser = subparsers.add_parser("add-task",help="Command to add a task")
    managetasks_parser.add_argument("TASK ", help="Task to be added")
    managetasks_parser.set_defaults(func=add_manage_tasks)

    addproject_parser = subparsers.add_parser("add-project", help= "add a project to user")
    addproject_parser.add_argument("username", help="The projects user")
    addproject_parser.add_argument("title",help="The project's title")
    addproject_parser.set_defaults(func=manage_projects)
    
    args = parser.parse_args()
    args.func(args)

