class Object(object):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, value):
        if not hasattr(self, '_initialized'):
            self.value = value
            self._initialized = True

    def __repr__(self):
        return f'{self.__class__.__name__}({self.value})'

obj1 = Object(10)
print(obj1)
obj2 = Object(20)
print(obj2)
print(obj1 is obj2)
print(obj1.value)