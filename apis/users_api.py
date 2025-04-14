import requests
from utils.config import BASE_URL


class UsersAPI:
    def __init__(self):
        self.url = f"{BASE_URL}/users"

    def get_all_users(self):
        return requests.get(self.url)

    def get_user_by_id(self, user_id):
        return requests.get(f"{self.url}/{user_id}")

    def create_user(self, data):
        return requests.post(self.url, json=data)

    def update_user(self, user_id, data):
        return requests.put(f"{self.url}/{user_id}", json=data)

    def delete_user(self, user_id):
        return requests.delete(f"{self.url}/{user_id}")
