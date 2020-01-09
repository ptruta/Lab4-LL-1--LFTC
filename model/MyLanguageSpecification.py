from typing import List, Any, Union, Dict

separators: List[Union[str, Any]] = ['[', ']', '{', '}', '(', ')', ':', ';', ' ', ',', '.']
operators = ['+', '-', '*', '/', '<', '>', '<=', '=', '>=', '==', '&&', '||', '%', '!', '!=', '^', '\n']
reservedWords = ['int', 'char', 'bool', 'array', 'float', 'struct', 'if', 'else', 'for', 'while', 'begin', 'end',
                 'read', 'write', 'string', 'epsilon']

everything = reservedWords + separators + operators
codification: Dict[str, int] = dict([[everything[i], i + 2] for i in range(len(everything))])
codification['identifier'] = 0
codification['constant'] = 1

print(codification)