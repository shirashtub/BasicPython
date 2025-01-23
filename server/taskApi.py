from flask import Blueprint, request, jsonify
from TaskManager import TaskManager
from Task import Task

task_bp = Blueprint('tasks', __name__)

tasks_manager = TaskManager()


@task_bp.route('/tasks', methods=['GET'])
def get_users():
    return jsonify(tasks_manager.to_dict()), 200


@task_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    if tasks_manager.get_task_by_id(task_id):
        return jsonify(tasks_manager.get_task_by_id(task_id).to_dict()), 200
    return {'error': f'not found task with task id: {task_id}'}, 404


@task_bp.route('/tasks', methods=['POST'])
def add_task():
    new_task = request.get_json()
    create_task = Task(new_task.get("title"), new_task.get("description"))
    tasks_manager.add_task(create_task)
    return jsonify(create_task.to_dict()), 201


@task_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def complete_task(task_id):
    if tasks_manager.get_task_by_id(task_id):
        tasks_manager.mark_task_completed(task_id)
        return jsonify(tasks_manager.get_task_by_id(task_id).to_dict()), 200
    return {'error': f'not found task with task id: {task_id}'}, 404


@task_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if tasks_manager.get_task_by_id(task_id):
        tasks_manager.delete_task(task_id)
        return {'message': f'task with task id: {task_id} deleted'}, 200
    return {'error': f'not found task with task id: {task_id}'}, 404

