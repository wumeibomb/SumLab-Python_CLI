
class User:
    user_list = []

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
#one to many relationship with projects
