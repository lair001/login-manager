from abc import ABCMeta
from login_manager.libs.metaclasses.Singleton import Singleton

class AbstractSingleton(ABCMeta, Singleton):
    pass
