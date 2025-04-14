import requests
from utils.config import BASE_URL


class PostsAPI:
    def __init__(self):
        self.url = f"{BASE_URL}/posts"

    def get_all_posts(self):
        return requests.get(self.url)

    def get_post_by_id(self, post_id):
        return requests.get(f"{self.url}/{post_id}")

    def create_post(self, data):
        return requests.post(self.url, json=data)
