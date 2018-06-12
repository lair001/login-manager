from abc import ABCMeta
from abc import abstractmethod


class FileContents(metaclass=ABCMeta):

    @abstractmethod
    def get_path(self):
        self.__class__.__default_method()

    @abstractmethod
    def get_contents(self):
        self.__class__.__default_method()

    @abstractmethod
    def update(self):
        self.__class__.__default_method()

    @classmethod
    @abstractmethod
    def get_instance(cls, path):
        cls.__default_method()

    @classmethod
    def __default_method(cls):
        raise NotImplementedError