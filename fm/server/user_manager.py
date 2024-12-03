class UserManager:
    def __init__(self):
        # 用于存储用户信息，简单起见存储为字典 {用户名: 密码}
        self.users = {"admin": "admin123", "test_user": "password"}

    def add_user(self, username, password):
        if username in self.users:
            return False  # 用户已存在
        self.users[username] = password
        return True

    def authenticate_user(self, username, password):
        return self.users.get(username) == password

    def manage_permissions(self, username, permissions):
        # 此处可以扩展为用户权限管理功能
        pass
