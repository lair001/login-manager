from login_manager.libs.metaclasses.Singleton import Singleton


class ActionStore(metaclass=Singleton):

    def __init__(self):
        self.__shoulds = {}

    def set_should_create_as_true(self):
        self.__set_should_as_true(self, 'create')

    def set_should_create_as_false(self):
        self.__set_should_as_false(self, 'create')

    def set_should_load_as_true(self):
        self.__set_should_as_true(self, 'load')

    def set_should_load_as_false(self):
        self.__set_should_as_false(self, 'load')

    def set_should_designate_default_as_true(self):
        self.__set_should_as_true(self, 'designate_default')

    def set_should_designate_default_as_false(self):
        self.__set_should_as_false(self, 'designate_default')

    def should_create(self):
        return self.__should(self, 'create')

    def should_load(self):
        return self.__should(self, 'load')

    def should_designate_default(self):
        return self.__should(self, 'designate_default')

    def clear(self):
        self.__shoulds.clear()

    # private methods

    def __set_should(self, action, boolean):
        self.shoulds[action] = boolean

    def __set_should_as_true(self, action):
        self.__set_should(action, True)

    def __set_should_as_false(self, action):
        self.__set_should(action, False)

    def __should(self, action):
        return self.__shoulds.get(action, False)

