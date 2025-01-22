class Task:

    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        return f"title: {self.title}, description: {self.description}, is completed? {self.completed}"
