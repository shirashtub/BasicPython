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

    def get_task_by_id(self, task_id):
        return self.tasks.get(task_id)

    def delete_task(self, task_id):
        if self.tasks.get(task_id):
            del self.tasks[task_id]
        else:
            print(f"task {task_id} not found")

    def to_dict(self):
        return {task_id: task.to_dict() for task_id, task in self.tasks.items()}
