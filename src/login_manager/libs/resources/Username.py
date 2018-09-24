import sys
import re
from login_manager.libs.resources.Resource import Resource


class Username(Resource):

    def __init__(self):
        pass

    def __str__(self):
        return self.username_str

    def load(self, username_str):
        self.username_str = self.__class__.validate(username_str)

    def create(self):
        super().create()

    def designate_default(self, username_str):
        self.load(username_str)

    __valid_username_regex = re.compile('\A[^@/~]{1,32}\Z')

    @classmethod
    def is_valid(cls, username_str):
        return re.match(cls.__valid_username_regex, username_str) is not None

    @classmethod
    def validate(cls, username_str):
        if cls.is_valid(username_str):
            return username_str
        else:
            print(f"The provided username is invalid: {username_str}")
            sys.exit(2)
