
class Project:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due = due_date
        self._tasks = []
        
#one to many relationship with tasks