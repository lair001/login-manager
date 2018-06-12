from login_manager.libs.resources.Resource import Resource


class Username(Resource):

    def __init__(self):
        pass

    def load(self, username_str):
        self.username_str = self.__class__.validate(username_str)

    def create(self):
        super().create()

    def designate_default(self, username_str):
        self.load(username_str)
