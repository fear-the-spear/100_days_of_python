import requests as req

class Post:
    def __init__(self):
        self.url = "https://api.npoint.io/fadd5ff9526b8ed9ee1f"

    def get_posts(self):
        res = req.get(url=self.url)
        posts = res.json()
        return posts