
class Tasks:
    def __init__(self, title, status, assigned_to):
        self.title = title
        self.status = status
        self.assigned_to = assigned_to
        
    def complete(self):
        self.completed = True
        print("task complete!!! feeling fulfilled?")
