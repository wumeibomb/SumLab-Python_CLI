import argparse
import json
#from tabulate import tabulate, why isn't this working...
from models import User, Tasks, Project
from datetime import datetime


#create users, projects and tasks
#display and search for projects
#structure commands logically with clear naming conventions and grouping.
#Use descriptive help text for every command and argument.
#Validate all user input to prevent incorrect usage or runtime errors.
#Offer default values and optional flags to increase flexibility.
#Handle exceptions with meaningful error messages, not cryptic stack traces.
#Avoid overwhelming the user—display only relevant info, and provide examples where helpful.

log_file = "data/main.json"

projects_list = {}
email_list = {}
user_list =  {}

def add_user(args):  
        
        new_user = {
            "id": f"{datetime.now().strftime("%H%M%S")}",
            "username": f"{args.USER}",
            "email": f"{args.EMAIL}",
            "projects": [{"tasks": []}]
        }

        def new_user_logging(bruh):
            with open(log_file,"r+") as file:
                userdata = json.load(file) 
                userdata["users"].append(new_user)
                file.seek(0)
                json.dump(userdata,file, indent=2)
                           #"email" : {gmail}}")
              #file.write(f"[{timestamp}] - New User Added : {username} & Email : {gmail}\n")
        new_user_logging(User)



#IF USER EXISTS 
def manage_projects(args):
    projects = {
         "title": f"{args.title}",
         "description": f"{args.description}",
         "due_date" : f"{args.duedate}"
     }

    def project_logging(project):
                
                with open(log_file,"r+") as file:
                    userdata = json.load(file)
                    for eachuserproject in userdata["users"]:
                        user_project = eachuserproject["projects"]
        
                    if user_project == "":
                        print("Please create a user first")

                    user_project.append(projects)
                    file.seek(0)
                    json.dump(userdata ,file, indent=2)
            #else:
                #print("Project with the same title already exists.")
         # print("User not in database, please make an account via the New command")
    project_logging(Project)


def manage_users(args):
    with open(log_file, "r") as file:
        users = json.load(file)
        for eachusername in users["users"]:
            username = eachusername["username"]
            if username == [] or users["users"] == []:
                print("No current users, please make an account using the New command")
            else:
                print(username)


def manage_tasks(args):
     task = {
          "TODO": f"{args.task}"
          }
     
     #completion
     with open(log_file,"r+") as file:
            userdata = json.load(file)
            for eachuserproject in userdata["users"]:

                user_tasks = eachuserproject["projects"]

        
                if user_tasks == "":
                   print("Please create a user first")
                        
                user_tasks.append(task)
                file.seek(0)
                json.dump(userdata ,file, indent=2)

     #projects = projects_list.get(args.USER)
     #if projects:
      #    for eachtask in projects.TASK:
       #        if eachtask.title == args.title:
        #            Tasks.complete()
          #          return
     

def add_manage_tasks(args):
        tasks = {
             "TODO": f"{args.task}"
        }
        print(tasks)

        with open(log_file,"r+") as data:
            userdata = json.load(data)

        if userdata["users"] == []:
            print("Can't create a task, no users or projects")

            for eachproject in userdata["users"]:
                item = eachproject["projects"]
                for eachitem in item:
                   user_tasks =  eachitem["tasks"]

                if user_tasks == []:
                    print("no tasks as of now!")
            user_tasks.append(tasks)
            data.seek(0)
            json.dump(userdata ,data, indent=2)


def main():

    parser = argparse.ArgumentParser(description= "Python Project Management CLI tool.")
# select them, display projects - assign task to projects and mark complete.
#if certain user selected, open this set of projects. don't show the others.
    subparsers = parser.add_subparsers()
    add_parser = subparsers.add_parser("New", help="Add a new USER!") #new user, no list of users
    add_parser.add_argument("USER", help="Name of the USER!") #what you write after New
    add_parser.add_argument("EMAIL", help="Email of the New User")
    add_parser.set_defaults(func=add_user)

    manageuser_parser = subparsers.add_parser("Users", help="Lists users")
    manageuser_parser.set_defaults(func=manage_users)

    managetasks_parser = subparsers.add_parser("add-task",help="Command to add a task: add-task taskname assignedproject")
    managetasks_parser.add_argument("task", help="Task to be added")
    managetasks_parser.add_argument("assignto", help="Project to assign the task to")
    managetasks_parser.set_defaults(func=add_manage_tasks)
    #need to complete tasks

    addproject_parser = subparsers.add_parser("add-project", help= "Add a project to user")
    addproject_parser.add_argument("User", help= "add project to this user")
    addproject_parser.add_argument("title",help="The project's title")
    addproject_parser.add_argument("description", help="Description of the project")
    addproject_parser.add_argument("duedate", help="Due date of the project")
    addproject_parser.set_defaults(func=manage_projects)

   
    #list projects under a user eg flopster has added this, then show othger projects if any.
    #add tasks to projects

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

