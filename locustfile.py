from locust import HttpUser, TaskSet, between

def index(l):
    l.client.get("/")

class UserBehavior(TaskSet):
    tasks = {index: 1}

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    min_wait = 400
    max_wait = 10000
