from login_manager.libs.metaclasses.AbstractSingleton import AbstractSingleton
from abc import abstractmethod

class Resource(metaclass=AbstractSingleton):

    @abstractmethod
    def load(self):
       self.__default_action('load')

    @abstractmethod
    def create(self):
       self.__default_action('create')

    @abstractmethod
    def designate_default(self):
       self.__default_action('designate_default')

    def __default_action(self, action):
        raise NotImplementedError("Action %s cannot be performed on %s." %(action, self.__class__.__name__))