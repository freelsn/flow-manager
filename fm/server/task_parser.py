import json
from fm.shared.models import TaskFlow

class TaskParser:
    def parse_json_config(self, config):
        config_data = json.loads(config)
        task_flow = TaskFlow()
        task_flow.build_flow_graph(config_data)
        return task_flow
