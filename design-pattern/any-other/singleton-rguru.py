
class SingletonMeta(type):
    """
    The singleton class can be implemented in different ways in python. Some possible
    methods include: base class, decorator, metaclass. We will use the metaclass because
    it is best suited for this purpose
    """

    _instances = {}
