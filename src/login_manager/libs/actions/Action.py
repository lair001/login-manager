from login_manager.libs.metaclasses.AbstractSingleton import AbstractSingleton
from abc import abstractmethod


class Action(metaclass=AbstractSingleton):

    @property
    @abstractmethod
    def type(self):
        pass

    def execute(self, resource, opt_arg):
        getattr(resource, self.type)(opt_arg)

