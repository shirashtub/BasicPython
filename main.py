from client.taskApiCheck import get_tasks, add_task, get_task_by_id, mark_task_complete, delete_task

print("hello!!")


response = add_task({"title": "task 4", "description": "task 4 description"})
print(f"add: {response}")

task_1 = get_task_by_id(2)
print(f"get by id {task_1}")

complete_task_1 = mark_task_complete(3)
print(f"complete task {complete_task_1}")

all_tasks = get_tasks()
print(all_tasks)

delete_task = delete_task(2)
print(f"delete: {delete_task}")

all_tasks_again = get_tasks()
print(all_tasks_again)
