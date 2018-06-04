from login_manager.libs.resources.Resource import Resource


class Username(Resource):

    def __init__(self):
        pass

    def load(self, username):
        self.username = username

    def designate_default(self, username):
        self.load(username)
