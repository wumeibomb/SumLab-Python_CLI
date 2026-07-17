
class User:
    user_list = []

    def __init__(self, name, email):
        self.name = name
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
#one to many relationship with projects
