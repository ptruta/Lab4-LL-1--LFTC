import re

from model.MyLanguageSpecification import operators, everything


def isStringWithoutQuotes(line, index):
    if index == 0:
        return False

    return line[index - 1] == '\\'


def isCharPartOfOperator(char):
    for operator in operators:
        if char in operator:
            return True

    return False


def getTokenForString(line, index):
    countQuote = 0
    token = ''

    while index < len(line) and countQuote < 2:
        if line[index] == '"' and not isStringWithoutQuotes(line, index):
            countQuote += 1
        token += line[index]
        index += 1

    return token, index


def getTokenForOperator(line, index):
    token = ''

    while index < len(line) and isCharPartOfOperator(line[index]):
        token += line[index]
        index += 1

    if token == '-' and isConstant(line[index]):
        token += line[index]
        index += 1

    return token, index


def generateToken(line, separators):
    token = ''
    index = 0

    while index < len(line):
        if line[index] == '"':
            if token:
                yield token
            token, index = getTokenForString(line, index)
            yield token
            token = ''

        elif line[index] in separators:
            if token:
                yield token
            token, index = line[index], index + 1
            yield token
            token = ''

        elif isCharPartOfOperator(line[index]):
            if token:
                yield token
            token, index = getTokenForOperator(line, index)
            yield token
            token = ''

        else:
            token += line[index]
            index += 1

    if token and len(token) <= 8:
        yield token


def isIdentifier(token):
    return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]){0,8}$', token) is not None or \
            re.match(r'^[a-zA-Z][a-zA-Z]{0,8}[0-9]{0,8}$', token) is not None


def isConstant(token):
    return re.match('^(0|[+\- ]*[1-9][0-9]*)$|^\'[a-zA-Z0-9]\'$|^\".+\"$', token) is not None

