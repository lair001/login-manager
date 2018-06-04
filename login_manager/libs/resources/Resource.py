from login_manager.libs.utils.Abstract import Abstract
from login_manager.libs.metaclasses.Singleton import Singleton

# Can't use ABC or ABCMeta with Singleton due to a metaclass conflict
class Resource(Abstract, metaclass=Singleton):

    def load(self):
       self.__default_action('load')

    def create(self):
       self.__default_action('create')

    def designate_default(self):
       self.__default_action('designate_default')

    def __default_action(self, action):
        raise NotImplementedError("Action %s cannot be performed on %s." %(action, self.__class__.__name__))