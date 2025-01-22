from Task import Task
from TaskManager import TaskManager


def test_create_task():
    try_task = Task("trying task", "try task complete testing")
    assert try_task.title == "trying task"
    assert try_task.description == "try task complete testing"
    assert not try_task.completed


def test_complete_task():
    try_task = Task("trying task", "try task complete testing")
    try_task.mark_completed()
    assert try_task.completed


def test_add_task():
    try_task_manager = TaskManager()
    try_task = Task("trying task", "try task complete testing")
    try_task_manager.add_task(try_task)
    assert try_task_manager.get_tasks()[try_task_manager.count] == try_task


def test_mark_task_completed():
    try_task_manager = TaskManager()
    try_task = Task("trying task", "try task complete testing")
    try_task_manager.add_task(try_task)
    try_task_manager.mark_task_completed(try_task_manager.count)
    assert try_task_manager.get_tasks()[try_task_manager.count].completed


def test_no_have_task_id():
    try_task_manager = TaskManager()
    try_task = Task("trying task", "try task complete testing")
    try_task_manager.add_task(try_task)
    try_task_manager.mark_task_completed(try_task_manager.count)
    invalid_id = 6
    try:
        assert try_task_manager.get_tasks()[invalid_id].completed
    except KeyError as e:
        assert str(e) == f"{invalid_id}"
    else:
        assert False
