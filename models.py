# I had made a folder thinking that models/ meant a directory but guess not...

class User:

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self._projects = []
        print(username,email)
    
    def add_project(self, project):
        self.projects.append(project)
        print(self.projects)
        
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
         #ended up not including a delete function...

class Project(User):

    def __init__(self, title, description, due_date):
        super().__init__(self.username, self.email)
        self.title = title
        self.description = description
        self.due = due_date
        self.tasks = []
        
    def add_task(self, task):
         self.tasks.append(task)
         print("brih")
    
    def del_project(self):
        del self._value

class Tasks:
    def __init__(self, title, status, assigned_to):
        self.title = title
        self.status = status
        self.assigned_to = assigned_to
        
    def complete(self):
        self.completed = True
        print("task complete!!! feeling fulfilled?")
    
   