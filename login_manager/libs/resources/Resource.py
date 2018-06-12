from login_manager.libs.metaclasses.AbstractSingleton import AbstractSingleton
from abc import abstractmethod


class Resource(metaclass=AbstractSingleton):

    @abstractmethod
    def load(self):
       self.__class__.__default_action('load')

    @abstractmethod
    def create(self):
       self.__class__.__default_action('create')

    @abstractmethod
    def designate_default(self):
       self.__class__.__default_action('designate_default')

    @classmethod
    @abstractmethod
    def is_valid(cls):
        cls.__default_method()

    @classmethod
    @abstractmethod
    def validate(cls):
        cls.__default_method()

    @classmethod
    def __default_method(cls):
        raise NotImplementedError

    @classmethod
    def __default_action(cls, action):
        raise NotImplementedError("Action %s cannot be performed on %s." %(action, cls.__name__))
