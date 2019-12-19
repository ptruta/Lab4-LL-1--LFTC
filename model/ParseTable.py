class ParseTable:
    def __init__(self):
        self.__table = {}

    def put(self, key, value):
        self.__table[key] = value

    def get(self, key):
        for entry in self.__table.values():
            if entry.getValue() is not None:
                currentKey = entry.getKey1()
                currentValue = entry.getValue()
                if currentKey[0] == key.getKey1() and currentKey[1] == key.getValue():
                    return currentValue
        return None

    def containsKey(self, key):
        result = False
        for currentKey in self.__table.keys():
            if currentKey.getKey1() == key.getKey1() and currentKey.getValue() == key.getValue():
                result = True
        return result

    def __str__(self):
        str1 = ""
        for key in self.__table.keys():
            for value in self.__table.values():
                if value is not None:
                    str1 += "M[" + key.getKey1() + ", " + key.getValue() + "] = [" + str(value) + "]\n"
                    #print("M[" + key.getKey1() + ", " + key.getValue() + "] = [" + str(value) + "]\n")

        return str1


