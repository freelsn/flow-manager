from fm.server.task_parser import TaskParser

class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.parser = TaskParser()

    def create_task_flow(self, task_config):
        task_flow = self.parser.parse_json_config(task_config)
        task_id = len(self.tasks) + 1
        self.tasks[task_id] = task_flow
        return task_id

    def get_task_status(self, task_id):
        task_flow = self.tasks.get(int(task_id))
        if not task_flow:
            return "Task not found"
        return task_flow.get_status()
