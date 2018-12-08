import sys
from login_manager.libs.metaclasses.Singleton import Singleton
from collections import deque


class ActionStore(metaclass=Singleton):

    def __init__(self):
        self.__actions = deque()

    def add(self, action):
        if action in self.__actions:
            print("Cannot perform the same action twice on the same resource.")
            sys.exit(2)
        self.__actions.append(action)

    def execute(self, resource, opt_arg):
        while len(self.__actions) > 0:
            self.__actions.popleft().execute(resource, opt_arg)
