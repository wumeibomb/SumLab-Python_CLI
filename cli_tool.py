import argparse
from models import class_User
from models import class_Tasks
from models import class_Project
from datetime import datetime


#create users, projects and tasks
#display and search for projects
#structure commands logically with clear naming conventions and grouping.
#Use descriptive help text for every command and argument.
#Validate all user input to prevent incorrect usage or runtime errors.
#Offer default values and optional flags to increase flexibility.
#Handle exceptions with meaningful error messages, not cryptic stack traces.
#Avoid overwhelming the user—display only relevant info, and provide examples where helpful.

log_file = "data/user_log.txt"
class User:

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self._projects = []
        print(username,email)
    
    
    @property
    def projects(self):
        return self._projects
    
    @projects.setter
    def projects(self, value):
        if not isinstance(value, Project):
            raise TypeError("Must be of the USER class")
        self._projects = value
    
    @projects.deleter
    def projects(self):
         print("to delete")
         del self._projects

class Project(User):

    def __init__(self, title, description, due_date):
        super().__init__(self.username, self.email)
        self.title = title
        self.description = description
        self.due = due_date
        self.tasks = []
    
    def assign_project(self, user):
         user.project = self
        
    def add_task(self, task):
         self.tasks.append(task)
         print("brih")

class Tasks:
    def __init__(self, title, status, assigned_to):
        self.title = title
        self.status = status
        self.assigned_to = assigned_to
        
    def complete(self):
        self.completed = True
        print("task complete!!! feeling fulfilled?")
   
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

        def addition_logging(bruh):
            timestamp = datetime.now().strftime("%d-%m-%Y at %H:%M:%S")
            with open("data/main.json","a") as file:
                file.write(f'"username" : "{username}", "email" : "{gmail}"')
                           #"email" : {gmail}}")
              #file.write(f"[{timestamp}] - New User Added : {username} & Email : {gmail}\n")
        addition_logging(User)


def manage_users(args):
        test = getattr(args,args.USER)
        print("fsdv", test)

#bruh = User()

def manage_projects(args):
     print(f"{args.username} added {args.title}")

     def project_logging(bruh):
        if args.title in log_file:
             with open(log_file, "a") as file:
                file.write(f"{args.username} added {args.title}\n")
        else:
             print("This project is already in the database.")
        project_logging(Project)


def manage_tasks(args):
     #completion
     projects = projects_list.get(args.USER)
     if projects:
          for eachtask in projects.TASK:
               if eachtask.title == args.title:
                    class_Tasks.complete()
                    return
     

def add_manage_tasks(args):
    task = (args.pro)
    task.add_manage_tasks(task)

def main():

    parser = argparse.ArgumentParser(description= "Python Project Management CLI tool.")
# options: create user DOME, manage users(display the users) and select them, display projects - assign task to projects and mark complete.
#if certain user selected, open this set of projects. don't show the others.
    subparsers = parser.add_subparsers()
    add_parser = subparsers.add_parser("New", help="Add a new USER!") #new user, no list of users
    add_parser.add_argument("USER", help="Name of the USER!") #what you write after New
    add_parser.add_argument("EMAIL", help="Email of the New User")
    add_parser.set_defaults(func=add_user)

    manageuser_parser = subparsers.add_parser("Users", help="Lists users")
    manageuser_parser.set_defaults(func=manage_users)

    managetasks_parser = subparsers.add_parser("add-task",help="Command to add a task: add-task taskname assignedproject")
    managetasks_parser.add_argument("TASK ", help="Task to be added")
    managetasks_parser.add_argument("ASSIGNTO", help="Project to assign the task to")
    managetasks_parser.set_defaults(func=add_manage_tasks)
    #need to complete tasks

    addproject_parser = subparsers.add_parser("add-project", help= "Add a project to user")
    addproject_parser.add_argument("title",help="The project's title")
    addproject_parser.add_argument("description", help="Description of the project")
    addproject_parser.add_argument("duedate", help="Due date of the project")
    addproject_parser.set_defaults(func=manage_projects)

    deleteproject_parser = subparsers.add_parser("del-project", help= "to delete project")
    deleteproject_parser.add_argument("PROJECT", help="Project to delete")
    deleteproject_parser.set_defaults(func=Project)
    #list projects under a user eg flopster has added this, then show othger projects if any.
    #add tasks to projects

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

