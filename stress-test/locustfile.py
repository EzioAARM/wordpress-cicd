from locust import HttpLocust, TaskSet, between

def index(l):
    l.client.get("/")

def p1(l):
    l.client.get("/?p=1")

class UserBehavior(TaskSet):
    tasks = {index: 2, p1: 1}

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5.0, 9.0)
