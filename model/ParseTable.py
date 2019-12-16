class ParseTable:
    def __init__(self):
        self.__table = {}

    def put(self, key, value):
        self.__table[key] = value

    def get(self, key):
        for entry in self.__table.values():
            if entry[1] is not None:
                currentKey = entry[0]
                currentValue = entry[1]
                if currentKey[0] == key[0] and currentKey[1] == key[1]:
                    return currentValue
        return None

    def containsKey(self, key):
        result = False
        for currentKey in self.__table.keys():
            if currentKey[0] == key[0] and currentKey[1] == key[1]:
                result = True
        return result

    def __str__(self):

        str = ""
        for entry in self.__table.values():
            if entry[1] is not None:
                key = entry[0]
                value = entry[1]
                str += "M[" + key[0] + ", " + key[1] + "] = [" + value[0] + ", " + value[1] + "]\n"

        return str


