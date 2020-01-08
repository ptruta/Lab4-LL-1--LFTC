class HashTable:
    def __init__(self):
        self.__content = []

    def __search(self, key):
        for entry in self.__content:
            if entry[0] == key:
                return entry

    def __str__(self):
        return str(self.__content)

    def add(self, value):
        key = self.hashCode(value)

        inddex = self.__search(key)

        if inddex is not None:
            listCol = inddex[1]
            if value not in listCol:
                listCol.append(value)
            return key, listCol.index(value)

        else:
            self.__content.append((key, [value]))
            col_index = 0
            return key, col_index

    def hashCode(self, value):
        return hash(value)

    def get(self, id):
        return self.__content[id]

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
