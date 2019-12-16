separators = ['[', ']', '{', '}', '(', ')', ':', ';', ' ', ',', '.']
operators = ['+', '-', '*', '/', '<', '>', '<=', '=', '>=', '==', '&&', '||', '%', '!', '!=', '^', '\n']
reservedWords = ['int', 'char', 'bool', 'array', 'float', 'struct', 'if', 'else', 'for', 'while', 'begin', 'end',
                 'read', 'write']

everything = reservedWords + separators + operators
codification = dict([[everything[i], i + 2] for i in range(len(everything))])
codification['identifier'] = 0
codification['constant'] = 1
