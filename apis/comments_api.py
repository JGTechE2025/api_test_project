import requests
from utils.config import BASE_URL


class CommentsAPI:
    def __init__(self):
        self.url = f"{BASE_URL}/comments"

    def get_all_comments(self):
        return requests.get(self.url)

    def get_comment_by_id(self, comment_id):
        return requests.get(f"{self.url}/{comment_id}")
