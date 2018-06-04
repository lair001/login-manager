# Used when metaclass conflicts prevent the use of ABC and ABCMeta
class Abstract():

    def __init__(self):
        raise NotImplementedError("Cannot instantiate abstract class %s." %(self.__class__.__name__))
