class Task:
    def __init__(self, task_id, name):
        self.task_id = task_id
        self.name = name
        self.status = "pending"
        self.dependencies = []

    def execute(self):
        self.status = "completed"

class TaskFlow:
    def __init__(self):
        self.tasks = []
        self.dependencies = {}

    def build_flow_graph(self, config_data):
        for task in config_data["tasks"]:
            task_obj = Task(task["id"], task["name"])
            self.tasks.append(task_obj)
            self.dependencies[task_obj] = task.get("dependencies", [])

    def get_status(self):
        return {task.name: task.status for task in self.tasks}
