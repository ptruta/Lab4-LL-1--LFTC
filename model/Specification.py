separators = ['(', ')', '[', ']', '{', '}', ';', ',', ' ', '\n']
operators = ['+', '-', '*', '/', '<', '<=', '==', '>=', '>', '!=', '=']
reservedWords = ['char', 'int', 'long', 'return', 'read', 'write', 'void', 'while', 'else', 'for', 'if', 'then']

everything = separators + operators + reservedWords
codification = dict([(everything[i], i + 2) for i in range(len(everything))])
codification['identifier'] = 0
codification['constant'] = 1
