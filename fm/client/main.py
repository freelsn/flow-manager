import requests

class Client:
    def __init__(self, server_url):
        self.server_url = server_url

    def login(self, username, password):
        response = requests.post(f"{self.server_url}/login", json={"username": username, "password": password})
        return response.json()

    def submit_task_config(self, task_config_path):
        with open(task_config_path, 'r') as file:
            task_config = file.read()
        response = requests.post(f"{self.server_url}/tasks", json={"config": task_config})
        return response.json()

    def view_task_status(self, task_id):
        response = requests.get(f"{self.server_url}/tasks/{task_id}")
        return response.json()


if __name__ == "__main__":
    client = Client(server_url="http://localhost:5000")
    print("Welcome to the Task Management Client")
    # Demo Login
    result = client.login("test_user", "password")
    print("Login Response:", result)
