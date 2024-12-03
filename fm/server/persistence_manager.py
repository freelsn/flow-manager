import json
import os

class PersistenceManager:
    def __init__(self, filepath="data.json"):
        self.filepath = filepath

    def save_state(self, data):
        """将任务和用户数据保存到文件"""
        with open(self.filepath, 'w') as file:
            json.dump(data, file)

    def load_state(self):
        """从文件中加载任务和用户数据"""
        if not os.path.exists(self.filepath):
            return None
        with open(self.filepath, 'r') as file:
            return json.load(file)
