from inspect import stack

from model.Grammar import Grammar
from model.Pair import Pair
from model.ParseTable import ParseTable

class Parser:
    rules = stack()

    def __init__(self):
        self.__grammar = Grammar()
        self.__firstSet = dict()
        self.__followSet = {}
        self.__parseTable = ParseTable()
        self.__productionsNumbered = {}
        self.__alpha = stack()
        self.__beta = stack()
        self.__pi = stack()
        self.generateFirstSet()
        self.generateFollowSets()
        self.createParseTable()

    def generateFollowSets(self):
        for nonTerminal in self.__grammar.get_non_terminals():
            self.__followSet[nonTerminal] = self.followOf(nonTerminal, nonTerminal)

    def generateFirstSet(self):
        for nonTerminal in self.__grammar.get_non_terminals():
            self.__firstSet[nonTerminal] = self.firstOf(nonTerminal)

    def firstOf(self, nonTerminal):
        if nonTerminal in self.__firstSet.keys():
            return self.__firstSet[nonTerminal]
        terminals = self.__grammar.get_terminals()
        temp = set()
        for production in self.__grammar.get_productions_for_non_terminal(nonTerminal):
            for rule in production.getRules():
                firstSymbol = rule[0]
                if firstSymbol == "ε":
                    temp.add("ε")
                elif firstSymbol in terminals:
                    temp.add(firstSymbol)
                else:
                    if firstSymbol == nonTerminal:
                        return temp
                    else:
                        temp.union(self.firstOf(firstSymbol))
        return temp

    def followOf(self, nonTerminal, initialNonTerminal):
        if nonTerminal in self.__followSet.keys():
            return self.__followSet[nonTerminal]
        temp = set()
        terminals = self.__grammar.get_terminals()

        if nonTerminal == self.__grammar.get_starting_symbol():
            temp.add("$")
        for production in self.__grammar.get_productions_containing_non_terminal(nonTerminal):
            productionLeft = production.getStart()
            for rule in production.getRules():
                ruleConflict = [nonTerminal]
                ruleConflict += rule
                if nonTerminal in rule and ruleConflict not in self.rules:
                    self.rules.append(ruleConflict)
                    indexNonTerminal = rule.index(nonTerminal)
                    temp.union(
                        self.followOperation(nonTerminal, temp, terminals, productionLeft, rule, indexNonTerminal,
                                             initialNonTerminal))
                    sublist = rule[indexNonTerminal + 1: -1]
                    if nonTerminal in sublist:
                        temp.union(self.followOperation(nonTerminal, temp, terminals, productionLeft, rule,
                                                        indexNonTerminal + 1 + sublist.index(nonTerminal),
                                                        initialNonTerminal))
                    self.rules.pop()
        return temp

    def followOperation(self, nonTerminal, temp, terminals, prodLeft, rule, indexNonTerminal, initialNonTerminal):
        if indexNonTerminal == len(rule) - 1:
            if prodLeft == nonTerminal:
                return temp
            if initialNonTerminal != prodLeft:
                temp.union(self.followOf(prodLeft, initialNonTerminal))
        else:
            nextSymbol = rule[indexNonTerminal + 1]
            if nextSymbol in terminals:
                temp.add(nextSymbol)
            else:
                if initialNonTerminal != nextSymbol:
                    firsts = set(self.__firstSet[nextSymbol])
                    if "ε" in firsts:
                        temp.union(self.followOf(nextSymbol, initialNonTerminal))
                        firsts.remove("ε")
                    temp.union(firsts)
        return temp

    def createParseTable(self):
        self.numberingProductions()
        columnSymbols = list(self.__grammar.get_non_terminals())
        columnSymbols.append("$")

        # M(a, a) = pop
        # M($, $) = acc
        self.__parseTable.put(Pair("$", "$"), Pair(list("acc"), -1))
        for terminal in self.__grammar.get_terminals():
            self.__parseTable.put(Pair(terminal, terminal), Pair(list("pop"), -1))

        #  1) M(A, a) = (α, i),
        # if:
        #
        # a) a ∈ first(α)
        # b) a != ε
        # c) A -> α
        # production
        # with index i
        #
        # 2) M(A, b) = (α, i), if:
        # a) ε ∈ first(α)
        # b) whichever
        # b ∈ follow(A)
        # c) A -> α
        # production
        # with index
        for key in self.__productionsNumbered.keys():
            for value in self.__productionsNumbered.values():
                rowSymbol = key.getKey1()
                rule = key.getValue()
                parseTableValue = Pair(rule, value)

                for columnSymbol in columnSymbols:
                    parseTableKey = Pair(rowSymbol, columnSymbol)

                    if rule[0] == columnSymbol and columnSymbol != "ε":
                        self.__parseTable.put(parseTableKey, parseTableValue)

                    elif rule[0] in self.__grammar.get_non_terminals() and columnSymbol in self.__firstSet.get(rule[0]):
                        if not self.__parseTable.containsKey(parseTableKey):
                            self.__parseTable.put(parseTableKey, parseTableValue)

                    else:
                        if rule[0] == "ε":
                            for b in self.__followSet.get(rowSymbol):
                                self.__parseTable.put(Pair(rowSymbol, b), parseTableValue)

                        else:
                            firsts = set()
                            for symbol in rule:
                                if symbol in self.__grammar.get_non_terminals():
                                    firsts.union(self.__firstSet.get(symbol))
                            if "ε" in firsts:
                                for b in self.__firstSet.get(rowSymbol):
                                    if b == "ε":
                                        b = "$"
                                    parseTableKey = Pair(rowSymbol, b)
                                    if not self.__parseTable.containsKey(parseTableKey):
                                        self.__parseTable.put(parseTableKey, parseTableValue)

    def parse(self, w):
        self.initializeStacks(w)

        go = True
        result = True

        while go:
            betaHead = self.__beta.pop()
            alphaHead = self.__alpha.pop()

            if betaHead == "$" and alphaHead == "$":
                return result

            heads = Pair(betaHead, alphaHead)
            parseTableInput = self.__parseTable.get(heads)

            if parseTableInput is None:
                heads = Pair(betaHead, "ε")
                parseTableInput = self.__parseTable.get(heads)
                if parseTableInput is not None:
                    self.__beta.pop()
                    continue

                if parseTableInput is None:
                    go = False
                    result = False
                else:
                    production = parseTableInput[0]
                    productionPos = parseTableInput[1]

                    if productionPos == -1 and production[0] == "acc":
                        go = False
                    elif productionPos == -1 and production[0] == "pop":
                        self.__beta.pop()
                        self.__alpha.pop()
                    else:
                        self.__beta.pop()
                        if production != "ε":
                            self.appendAsChars(production, self.__beta)
                        self.__pi.append(str(productionPos))
        return result

    def numberingProductions(self):
        index = 1
        for production in self.__grammar.get_productions():
            for rule in production.getRules():
                self.__productionsNumbered[Pair(production.getStart(), rule)] = index
                index += 1

    def initializeStacks(self, w):
        self.__alpha.clear()
        self.__alpha.append("$")
        self.appendAsChars(w, self.__alpha)

        self.__beta.clear()
        self.__beta.append("$")
        self.__beta.append(self.__grammar.get_starting_symbol())

        self.__pi.clear()
        self.__pi.append("ε")

    @staticmethod
    def appendAsChars(sequence, stack):
        for i in range(len(sequence) - 1, 0, -1):
            stack.append(sequence[i])

    def parseSource(self, pif):
        sequence = []
        for pifEntry in pif:
            sequence.append(str(pifEntry[0]))
        return self.parse(sequence)

    def getGrammar(self):
        return self.__grammar

    def getFollowSet(self):
        return self.__followSet

    def getFirstSet(self):
        return self.__firstSet

    def getParseTable(self):
        return self.__parseTable

    def getPi(self):
        return self.__pi

    def getProductionNumbered(self):
        return self.__productionsNumbered
