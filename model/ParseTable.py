class ParseTable:
    def __init__(self):
        self.__table = {}

    def put(self, key, value):
        self.__table[key] = value

    def get(self, key):
        for entry in self.__table:
            if self.__table[entry] is not None:
                currentKey = entry
                currentValue = self.__table[entry]
                if currentKey.getKey() == key.getKey() and currentKey.getValue() == key.getValue():
                    return currentValue
        return None

    def containsKey(self, key):
        result = False
        for currentKey in self.__table.keys():
            if currentKey.getKey() == key.getKey() and currentKey.getValue() == key.getValue():
                result = True
        return result

    def __str__(self):
        str1 = ""
        idx = 1
        for key in self.__table.keys():
            value = self.__table[key]
            if value is not None:
                str1 += str(idx) + ": M[" + key.getKey() + ", " + key.getValue() + "] = [" + str(value) + "]\n"
                idx += 1

        return str1
