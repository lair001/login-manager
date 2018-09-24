from login_manager.libs.metaclasses.Singleton import Singleton


class ActionStore(metaclass=Singleton):

    def __init__(self):
        self.__shoulds = {}

    def set_should_create_as_true(self):
        self.__set_should_as_true('create')

    def set_should_create_as_false(self):
        self.__set_should_as_false('create')

    def set_should_load_as_true(self):
        self.__set_should_as_true('load')

    def set_should_load_as_false(self):
        self.__set_should_as_false('load')

    def set_should_designate_default_as_true(self):
        self.__set_should_as_true('designate_default')

    def set_should_designate_default_as_false(self):
        self.__set_should_as_false('designate_default')

    def should_create(self):
        return self.__should('create')

    def should_load(self):
        return self.__should('load')

    def should_designate_default(self):
        return self.__should('designate_default')

    def clear(self):
        self.__shoulds.clear()

    # private methods

    def __set_should(self, action, boolean):
        self.__shoulds[action] = boolean

    def __set_should_as_true(self, action):
        self.__set_should(action, True)

    def __set_should_as_false(self, action):
        self.__set_should(action, False)

    def __should(self, action):
        return self.__shoulds.get(action, False)

