
class Project:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due = due_date
        self.tasks = []
    
    def assign_project(self, user):
         user.project = self
        
    def add_task(self, task):
         self.tasks.append(task)
         print("brih")
#class Project:
#    def __init__(self, title, description, due_date):
 #       self.title = title
  #      self.description = description
   #     self.due = due_date
    #    self._tasks = []
        
#one to many relationship with tasks