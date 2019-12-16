class SymbolTable:
    def __init__(self):
        self.__data = {}

    def getId(self, value):
        if value in self.__data.values():
            return hash(value)
        return -1

    def getValue(self, id):
        try:
            return self.__data[id]
        except KeyError:
            return -1

    def add(self, value):
        i = self.getId(value)
        if i != -1:
            return i
        else:
            self.__data[hash(value)] = value
            return hash(value)

    def __str__(self):
        return str(self.__data)
