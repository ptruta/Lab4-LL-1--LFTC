from model.HashTable.HashTable import HashTable


class SymbolTable:
    def __init__(self):
        self.__hashTable = HashTable()

    def __str__(self):
        return str(self.__hashTable)

    def add(self, value):
        return self.__hashTable.add(value)

    def get(self, value):
        return self.__hashTable.getID(value)

    def getHashTable(self):
        return self.__hashTable.getHashTable()
