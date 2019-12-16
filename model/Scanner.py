import re

from model.Specification import *

"""
    Checks if a "-" sign is used as an arithmetic operator or to denote a negative number
    :param line -> the line on which the minus sign is 
    :param index -> index of the minus sign in that line
"""


def isNegativeNumber(line, index):
    before = 0
    while isPartOfOperator(line[index - before]):
        if line[index - before] in operators:
            return True
        before += 1

    return False


"""
    checks if a character is part of an operator
    :param char -> the character which is evaluated   
"""


def isPartOfOperator(char):
    for op in operators:
        if char in op:
            return True
    return False


"""
    checks if an identifier verifies the language specification constraints
"""


def isIdentifier(token):
    return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]|_){,249}$', token) is not None


"""
    checks if an constant verifies the language specification constraints
"""


def isConstant(token):
    return re.match('^(0|[+-]?[1-9][0-9]*)$|^\'[a-zA-Z0-9]\'$|^\"[a-zA-Z0-9]\"$', token) is not None


"""
    delimits and returns a string token, which is bounded by two quotes
    :param line ->line on which the token is
    :param index ->index of the first quote
"""


def getStringToken(line, index):
    token = ""
    quotes = 0

    while index < len(line) and quotes < 2:
        if line[index] == '"':
            quotes += 1

        token += line[index]
        index += 1

    return token, index


"""
    returns an operator token 
    :param line ->line on which the token is
    :param index ->index of the first(if more) character of the token

"""


def getOperatorToken(line, index):
    token = ""

    while index < len(line) and isPartOfOperator(line[index]) and line[index] != "-":
        token += line[index]
        index += 1
    return token, index


"""
    iterates through a line and splits it into tokens
    :param line -> line that is manipulated 
"""


def tokenGenerator(line):
    token = ""
    index = 0

    while index < len(line):
        if line[index] == '"':
            if token:
                yield token
            token, index = getStringToken(line, index)

            yield token
            token = ''

        if line[index] == "-":
            if isNegativeNumber(line, index):
                token += line[index]
                index += 1
            else:

                yield token

        elif isPartOfOperator(line[index]):
            if token:
                yield token
            token, index = getOperatorToken(line, index)

            yield token
            token = ''

        elif line[index] in separators:
            if token:
                yield token
            token, index = line[index], index + 1

            yield token
            token = ''

        else:
            token += line[index]
            index += 1
    if token:
        yield token
