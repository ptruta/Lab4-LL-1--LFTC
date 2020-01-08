from typing import List, Any, Union, Dict

separators = []
operators = ['=', '<>', ':=', '\n']
reservedWords = ['if', 'then', 'else', 'epsilon']

everything = reservedWords + separators + operators
codification: Dict[str, int] = dict([[everything[i], i + 2] for i in range(len(everything))])
codification['identifier'] = 0
codification['constant'] = 1

print(codification)
