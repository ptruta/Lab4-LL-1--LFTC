import math


class HashTable:
    def __init__(self):
        self.__content = []

    def __search(self, key):
        return self.__content.index(key) if key in self.__content else None

    def __str__(self):
        return str(self.__content)

    def add(self, value):
        key = self.hashCode(value)

        inddex = self.__search(key)

        if inddex is not None:
            listCol = self.__content[inddex]
            if value not in listCol:
                listCol.append(value)
            return inddex, listCol.index(value)

        else:
            self.__content.append((key, [value]))
            col_index = 0
            index = len(self.__content) - 1
            return (index, col_index)

    def hashCode(self, value):
        sumOfCharsInt = 0

        for elementChar in value:
            # ascii code for characters, is the integer representation of A from ascii code
            sumOfCharsInt += ord(elementChar)

        return math.ceil(sumOfCharsInt / len(value))

    def getID(self, value):
        key = self.hashCode(value)
        index = self.__search(key)

        if index is None:
            return None

        colList = self.__content[index]

        if value not in colList:
            return None

        col_index = colList.index(value)

        return (index, col_index)

    def getHashTable(self):
        return self.__content


