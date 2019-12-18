class Pair:
    def __init__(self, key, value):
        self.__key = key
        self.__value = value

    def getKey1(self):
        return self.__key

    def setKey(self, key):
        self.__key = key

    def getValue(self):
        return self.__value

    def setValue(self, value):
        self.__value = value

    def __str__(self):
        return str(self.__key) + "=" + str(self.__value)
