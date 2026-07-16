import argparse

#create users, projects and tasks
#display and search for projects
#structure commands logically with clear naming conventions and grouping.
#Use descriptive help text for every command and argument.
#Validate all user input to prevent incorrect usage or runtime errors.
#Offer default values and optional flags to increase flexibility.
#Handle exceptions with meaningful error messages, not cryptic stack traces.
#Avoid overwhelming the user—display only relevant info, and provide examples where helpful.

def add_task(args):
    print(f"Added user {args.USER}")

def main():
    parser = argparse.ArgumentParser(description= "Python Project Management CLI tool.")
# options: create user, manage users(display the users) and select them, display projects - assign task to projects and mark complete.
#if certain user selected, open this set of projects. don't show the others.
    subparsers = parser.add_subparsers()
    add_parser = subparsers.add_parser("New", help="Add a new USER!")
    add_parser.add_argument("USER", help="Name of the USER!")
    
    add_parser.set_defaults(func=add_task)

    manageuser_parser = subparsers.add_parser("--Users", help="Lists users")
    manageuser_parser.add_argument("")
    args = parser.parse_args()
    args.func(args)

