from flask import Blueprint, request, jsonify
from TaskManager import TaskManager

task_bp = Blueprint('tasks', __name__)

tasks_manager = TaskManager()


@task_bp.route('/tasks', methods=['GET'])
def get_users():
    return jsonify(tasks_manager.get_tasks()), 200


@task_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_user_by_id(task_id):
    return tasks_manager.get_task_by_id(task_id), 200


@task_bp.route('/tasks', methods=['POST'])
def add_task():
    new_task = request.get_json()
    tasks_manager.add_task(new_task)
    return new_task, 201


@task_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def complete_task(task_id):
    tasks_manager.mark_task_completed(task_id)
    return tasks_manager.get_task_by_id(task_id), 200


@task_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks_manager.delete_task(task_id)
    return '', 204

