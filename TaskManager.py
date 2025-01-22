class TaskManager:

    def __init__(self):
        self.tasks = {}
        self.count = 0

    def add_task(self, task):
        self.count += 1
        self.tasks[self.count] = task

    def get_tasks(self):
        return self.tasks

    def mark_task_completed(self, task_id):
        if self.tasks.get(task_id):
            self.tasks.get(task_id).mark_completed()
        else:
            print(f"task {task_id} not found")

