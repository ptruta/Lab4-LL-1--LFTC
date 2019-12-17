from model.Parser import Parser
from model.Scanner import Scanner


class Program:
    parser = Parser()
    scanner = Scanner("./model/file.txt")

    def getFirstSet(self):
        return self.parser.getFirstSet()

    def getNonTerminals(self):
        return self.parser.getGrammar().get_non_terminals()

    def getTerminals(self):
        return self.parser.getGrammar().get_terminals()

    def getProductions(self):
        return self.parser.getGrammar().get_productions()

    def getProductionsForNonterminal(self, nonTerminal):
        return self.parser.getGrammar().get_productions_for_non_terminal(nonTerminal)

    def getStartingSymbol(self):
        return self.parser.getGrammar().get_starting_symbol()

    def getFollowSet(self):
        return self.parser.getFollowSet()

    def getParserTable(self):
        return self.parser.getParseTable()

    def parse(self, w):
        result = self.parser.parse(w)

        if result:
            print("Sequence" + str(w) + "accepted." + "\n")
            pi = self.parser.getPi()
            print("Pi" + str(pi) + "\n")
            print("Display productions of pi:" + str(self.displayPiProductions(pi)))

        else:
            print("Sequence " + str(w) + " is not accepted.")

    def displayPiProductions(self, pi):
        sb = ""

        for productionIndexString in pi:
            if productionIndexString == "ε":
                continue
            productionIndex = int(productionIndexString)
            for (key, value) in self.parser.getProductionNumbered():
                if productionIndex == value:
                    sb += str(value) + ": " + str(key.getKey()) + " -> " + \
                        str(key.getValue()) + "\n"

        return str(sb)

    def scanSourceCode(self):
        errors = self.scanner.run()

        if errors.size == 0:
            pif = self.scanner.getPif()
            print(pif + "\n")

            w = []
            for elem in pif:
                w.append(str(elem.getKey()))

            print(w)
            self.parse(w)

            return pif
        else:
            for error in errors:
                print(error)

        return None



    def parserPIF(self):
        pif = self.scanSourceCode()

        if pif is not None:
            print(self.parser.parseSource())
