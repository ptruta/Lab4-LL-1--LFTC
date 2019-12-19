import re

from model.HashTable.SymbolTable import SymbolTable
from model.MyLanguageSpecification import *
from model.Pair import Pair


class Scanner:

    def __init__(self, fileName):
        self.__pif = []
        self.__constantTable = SymbolTable()
        self.__identifierTable = SymbolTable()
        self.__fileName = fileName

    @staticmethod
    def getOperatorToken(line, index):
        token = ""

        while index < len(line) and Scanner.isPartOfOperator(line[index]) and line[index] != "-":
            token += line[index]
            index += 1
        return token, index

    @staticmethod
    def getStringToken(line, index):
        token = ""
        quotes = 0

        while index < len(line) and quotes < 2:
            if line[index] == '"':
                quotes += 1

            token += line[index]
            index += 1

        return token, index

    @staticmethod
    def isIdentifier(token):
        return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]){0,8}$', token) is not None or \
               re.match(r'^[a-zA-Z][a-zA-Z]{0,8}[0-9]{0,8}$', token) is not None
    @staticmethod
    def isConstant(token):
        return re.match('^(0|[+\- ]*[1-9][0-9]*)$|^\'[a-zA-Z0-9]\'$|^\".+\"$', token) is not None

    @staticmethod
    def isPartOfOperator(char):
        for op in operators:
            if char in op:
                return True
        return False

    @staticmethod
    def isNegativeNumber(line, index):
        before = 0
        while Scanner.isPartOfOperator(line[index - before]):
            if line[index - before] in operators:
                return True
            before += 1

        return False

    @staticmethod
    def tokenGenerator(line):
        token = ""
        index = 0

        while index < len(line):
            if line[index] == '"':
                if token:
                    yield token
                token, index = Scanner.getStringToken(line, index)

                yield token
                token = ''

            if line[index] == "-":
                if Scanner.isNegativeNumber(line, index):
                    token += line[index]
                    index += 1
                else:

                    yield token

            elif Scanner.isPartOfOperator(line[index]):
                if token:
                    yield token
                token, index = Scanner.getOperatorToken(line, index)

                yield token
                token = ''

            elif line[index] in separators:
                if token:
                    yield token
                token, index = line[index], index + 1

                yield token
                token = ''

            elif line[index] in reservedWords:
                if token:
                    yield token
                token, index = line[index], index + 1

                yield token
                token = ''

            else:
                token += line[index]
                index += 1

        if token and len(token) <= 8:
            yield token

    def getPif(self):
        return self.__pif

    def getConstantTable(self):
        return self.__constantTable

    def getIdentifierTable(self):
        return self.__identifierTable

    def displayPifReadable(self):
        pifReadable = []
        for pair in self.__pif:
            codificationTableCode = int(pair.getKey())
            symbolTablePosition = int(pair.getValue())
            codificationTableToken = Scanner.findKeyInCodificationTable(codificationTableCode)
            if symbolTablePosition == -1:
                pifReadable.append(Pair(codificationTableToken + " " + str(codificationTableCode), "from Codification"))

            elif symbolTablePosition == 0:
                symbolTableEntry = self.__identifierTable.getValue(symbolTablePosition)
                pifReadable.append(
                    Pair(codificationTableToken + " " + str(codificationTableCode), " " + str(symbolTableEntry)))
            elif symbolTablePosition == 1:
                symbolTableEntry = self.__constantTable.get(symbolTablePosition)
                pifReadable.append(
                    Pair(codificationTableToken + " " + str(codificationTableCode), " " + str(symbolTableEntry)))

        print("Program Internal Form readable: " + str(pifReadable))

    @staticmethod
    def removeExtraSpaces(line):
        return line.strip().replace(" {2,}", " ")

    @staticmethod
    def findKeyInCodificationTable(value):
        for key in codification.keys():
            for value1 in codification.values():
                if value1 == value:
                    return key

    def run(self):

        errors = []
        lineNr = 1
        try:
            with open(self.__fileName, "r") as file:
                for line in file.readlines():
                    line = Scanner.removeExtraSpaces(line)
                    for token in self.tokenGenerator(line):
                        if token in everything:
                            self.__pif.append(Pair(codification[token], -1))
                        elif Scanner.isIdentifier(token):
                            self.__pif.append(
                                Pair(codification["identifier"], self.__identifierTable.add(token)[0]))
                        elif Scanner.isConstant(token):
                            self.__pif.append(Pair(codification['constant'], self.__constantTable.add(token)[0]))
                        else:
                            errors.append("Unknown token: " + token + " at line :" + str(lineNr))

                lineNr += 1

        except IOError as e:
            print(e)
        return errors
