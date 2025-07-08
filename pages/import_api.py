import requests

class ImportAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json"
        }

    def import_user(self, user_id):
        payload = {
            "userId": user_id,
            "title": "testing",
            "body": "challenge automation"
        }
        response = requests.post(f"{self.base_url}/posts", json=payload, headers=self.headers)
        return response
