# from model.HashTable.HashTable import HashTable
# from model.HashTable.SymbolTable import SymbolTable
# import re
#
#
# class Scanner:
#     SOURCEFILEPATH = "./data/source.txt"
#     CODIFICATIONFILEPATH = "./data/codification.txt"
#
#     def __init__(self):
#         self.__codification = []
#         self.__symboltable = SymbolTable()
#         self.__pif = []
#         self.getCodification()
#
#     def getCodification(self):
#         with open(self.CODIFICATIONFILEPATH) as f:
#             self.__codification += f.readlines()
#
#         print("Language codification: " + str(self.__codification) + "\n")
#
#     def getPif(self):
#         return self.__pif
#
#     def removeExtraSpaces(self, line):
#         return line.strip().replace(" {2,}", " ")
#
#     def displayPifReadable(self, pif):
#         pifReadable = []
#         for pair in pif:
#             codificationTableCode = int(pair[0])
#             symbolTablePosition = int(pair[1])
#             codificationTableToken = self.__codification[codificationTableCode]
#             if symbolTablePosition == -1:
#                 pifReadable.append((codificationTableToken + " " + codificationTableCode, "from Codification"))
#             else:
#                 symbolTableEntry = self.__symboltable.get(symbolTablePosition)
#                 pifReadable.append((codificationTableToken + " " + codificationTableCode, " " + symbolTableEntry))
#
#         print("Program Internal Form readable: " + str(pifReadable))
#
#     @staticmethod
#     def lastIndexOf(elem, list):
#         return max(loc for loc, val in enumerate(list) if val == elem)
#
#     @staticmethod
#     def splitMinus(s, allTokens):
#         if s.find("-") and len(s) != 1:
#             tokens = s.split("-")
#             # removeIf(s1->s1.equals("")) cplm ar trebui sa faca asta?
#             for i in range(len(tokens)):
#                 allTokens.append((Scanner.lastIndexOf(s, allTokens) + 1, tokens[i]))
#                 pos = Scanner.lastIndexOf(tokens[i], allTokens)
#
#                 pattern = re.compile("-?\\d+")
#                 if not pattern.match(allTokens[pos - 1]) and i < len(tokens) - 1:
#                     allTokens.append(Scanner.lastIndexOf(tokens[i], allTokens) + 1, "-" + tokens[i + 1])
#                     i += 1
#                 elif i < len(tokens) - 1 or len(tokens) == 1:
#                     allTokens.append(Scanner.lastIndexOf(tokens[i], allTokens) + 1, "-")
#             allTokens.remove(s)
#
#     @staticmethod
#     def splitGreater(s, allTokens):
#         if s.find(">") and len(s) != 1 and not s.find(">="):
#             tokens = s.split(">")
#             for i in range(len(tokens)):
#                 allTokens.append(Scanner.lastIndexOf(s, allTokens), tokens[i])
#                 if i < len(tokens) - 1 or len(tokens) == 1:
#                     allTokens.append(Scanner.lastIndexOf(tokens[i], allTokens) + 1, ">")
#             allTokens.remove(s)
#
#     @staticmethod
#     def splitLess(s, allTokens):
#         if s.find("<") and len(s) != 1 and not s.find("<="):
#             tokens = s.split("<")
#             for i in range(len(tokens)):
#                 allTokens.append(Scanner.lastIndexOf(s, allTokens), tokens[i])
#                 if i < len(tokens) - 1 or len(tokens) == 1:
#                     allTokens.append(Scanner.lastIndexOf(tokens[i], allTokens) + 1, "<")
#             allTokens.remove(s)
#
#     @staticmethod
#     def splitColon(s, allTokens):
#         if s.find(":") and len(s) != 1:
#             tokens = s.split(":")
#             for i in range(len(tokens)):
#                 allTokens.append(Scanner.lastIndexOf(s, allTokens), tokens[i])
#                 if i < len(tokens) - 1 or len(tokens) == 1:
#                     allTokens.append(Scanner.lastIndexOf(tokens[i], allTokens) + 1, ":")
#             allTokens.remove(s)
#
#     @staticmethod
#     def splitEqual(s, allTokens):
#         if s.find("=") and len(s) != 1 and not s.find(">=") and not s.find("<="):
#             tokens = s.split("=")
#             for i in range(len(tokens)):
#                 if tokens[i] != "":
#                     allTokens.append(allTokens.index(s) + 1, tokens[i])
#                 if i % 2 == 0:
#                     allTokens.append(allTokens.index(s), "=")
#         allTokens.remove(s)
#
#     def indentify(self, part):
#         if part in self.__codification:
#             self.__pif.append((self.__codification[part], -1))
#         else:
#             if Scanner.isStCandidate(part):
#                 if self.__symboltable.get(part):
#
#
#
#     @staticmethod
#     def isStCandidate(part):
#         if Scanner.isConstant(part):
#             return True
#         else:
#             if len(part) <= 8:
#                 if Scanner.isIdentifier(part):
#                     return True
#                 else:
#                     raise NameError()
#             else:
#                 raise ValueError()
#     @staticmethod
#     def isIdentifier(part):
#         pattern = re.compile("(^[a-zA-Z]+[_0-9a-zA-Z]*)")
#         return pattern.match(part)
#
#     @staticmethod
#     def isConstant(part):
#         pattern1 = re.compile("-?[1-9]+[0-9]*|0")
#         pattern2 = re.compile("'[1-9a-zA-Z]'")
#         pattern3 = re.compile("\"[1-9a-zA-Z]+\"")
#         return pattern1.match(part) or pattern2.match(part) or pattern3.match(part)
