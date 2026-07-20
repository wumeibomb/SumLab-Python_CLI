import class_Project
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
        if not isinstance(value, class_Project):
            raise TypeError("Must be of the USER class")
        self._projects = value
    
    @projects.deleter
    def projects(self):
         print("to delete")
         del self._projects

#one to many relationship with projects
