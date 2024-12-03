from flask import Flask, request, jsonify
from fm.server.task_manager import TaskManager
from fm.server.user_manager import UserManager
from fm.server.persistence_manager import PersistenceManager

app = Flask(__name__)
task_manager = TaskManager()
user_manager = UserManager()
persistence_manager = PersistenceManager()

# Load state at server startup
saved_state = persistence_manager.load_state()
if saved_state:
    # 假设状态包括任务和用户信息
    task_manager.tasks = saved_state.get("tasks", {})
    user_manager.users = saved_state.get("users", {})

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    success = user_manager.authenticate_user(username, password)
    return jsonify({"success": success})

@app.route("/tasks", methods=["POST"])
def submit_task():
    data = request.json
    task_config = data.get("config")
    task_id = task_manager.create_task_flow(task_config)
    # 持久化任务状态
    persistence_manager.save_state({"tasks": task_manager.tasks, "users": user_manager.users})
    return jsonify({"task_id": task_id})

@app.route("/tasks/<task_id>", methods=["GET"])
def get_task_status(task_id):
    status = task_manager.get_task_status(task_id)
    return jsonify({"task_id": task_id, "status": status})

if __name__ == "__main__":
    app.run(debug=True)
