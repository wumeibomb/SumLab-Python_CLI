import argparse
from models import class_User
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

    def __init__(self, username, email):
        self.username = username
        self.email = email
        print(username,email)
    
    @property
    def projects(self):
        return self._projects
    
    @projects.setter
    def projects(self, value):
        if not isinstance(value, Project):
            raise TypeError("Must be of the USER class")
        self._projects = value



projects_list = {}
email_list = {}
user_list = {}

def add_user(args):  
        user = User(args.USER, args.EMAIL)
        user_list[args.USER] = user

        username = args.USER
        gmail = args.EMAIL

        email = email_list.get(args.EMAIL)
        email_list[args.EMAIL]= email

        with open("data/user_log.txt","w") as test:
              test.write(f"New User Added : {username} & Email : {gmail}")

        #ITS NOT ADDING MORE TO THE LIST OH MY GOSHHHH

def manage_users(args):
        users = user_list
        print(users)

def manage_projects(args):
     print(f"{args.username} added {args.title}")

def manage_tasks(args):
     #completion or deletion?
     projects = projects_list.get(args.USER)
     if projects:
          for eachtask in projects.TASK:
               if eachtask.title == args.title:
                    task.complete()
                    return
     
def add_manage_tasks(args):
    task = (args.pro)
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

    managetasks_parser = subparsers.add_parser("add-task",help="Command to add a task: add-task taskname assignedproject")
    managetasks_parser.add_argument("TASK ", help="Task to be added")
    managetasks_parser.add_argument("ASSIGNTO", help="Project to assign the task to")
    managetasks_parser.set_defaults(func=add_manage_tasks)
    #need to complete tasks

    addproject_parser = subparsers.add_parser("add-project", help= "add a project to user")
    addproject_parser.add_argument("username", help="The projects user")
    addproject_parser.add_argument("title",help="The project's title")
    addproject_parser.set_defaults(func=manage_projects)
    #list projects under a user eg flopster has added this, then show othger projects if any.
    #add tasks to projects

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

