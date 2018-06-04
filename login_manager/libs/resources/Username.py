from login_manager.libs.resources.Resource import Resource
from login_manager.libs.metaclasses.Singleton import Singleton


class Username(Resource):

    def __init__(self):
        pass

    def load(self, username):
        self.username = username

    def designate_default(self, username):
        self.load(username)
