from typing import OrderedDict

class MyUniqueObject():
    _instance = None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls()
        
        return cls._instance


if __name__ == "__main__":

    var1 = MyUniqueObject.get_instance()

    var2 = MyUniqueObject.get_instance()

    print(id(var1) == id(var2))
    