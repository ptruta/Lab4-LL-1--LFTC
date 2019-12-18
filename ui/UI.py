from controller.Program import Program


class UI:
    def __init__(self, program):
        self.program = program

    def start(self):
        print("\n")
        print("\t 0 - Exit \n")
        print("\t 1 - Grammar \n")
        print("\t 2 - Parser \n")

        option = int(input("Your choice is:"))

        if option == 0:
            exit(0)
        elif option == 1:
            self.fileMenuGrammar()
            return
        elif option == 2:
            self.fileMenuParser()
            return
        self.start()

    def fileMenuGrammar(self):
        print()
        print("\t0 - Back \n")
        print("\t1 - Non-terminals \n")
        print("\t2 - Terminals \n")
        print("\t3 - Productions \n")
        print("\t4 - Productions of a non-terminal \n")
        print("\t5 - Starting Symbol \n")

        option = int(input("Your choice is:"))

        if option == 0:
            self.start()
            return
        elif option == 1:
            print(str(self.program.getNonTerminals()) + "\n")
            print("\n")
            self.fileMenuGrammar()
            return
        elif option == 2:
            print(str(self.program.getTerminals()) + "\n")
            print("\n")
            self.fileMenuGrammar()
            return
        elif option == 3:
            print("P :{ \n")
            for production in self.program.getProductions():
                print("     "+ str(production))
            print("} + \n")
            print("\n")
            self.fileMenuGrammar()
            return
        elif option == 4:
            print(str(self.program.getProductionsForNonterminal(self.promptForSequence()))+"\n")
            print("\n")
            self.fileMenuGrammar()
            return
        elif option == 5:
            print(str(self.program.getStartingSymbol())+"\n")
            print("\n")
            self.fileMenuGrammar()
            return
        self.start()


    def fileMenuParser(self):
        print()
        print("\t0 - Back \n")
        print("\t1 - Get FIRST set \n")
        print("\t2 - Get FOLLOW set \n")
        print("\t3 - Create parse table \n")
        print("\t4 - Parse sequence \n")
        print("\t5 - Parse source code \n")
        print("\t6 - Parse pif \n")

        option = int(input("Your choice is:"))

        if option == 0:
            self.start()
            return
        elif option == 1:
            for (key,value) in self.program.getFirstSet():
                print(self.displaySet(key,value))
            self.fileMenuParser()
            return
        elif option == 2:
            for (key,value) in self.program.getFollowSet():
                print(self.displaySet(key,value))
            self.fileMenuParser()
            return
        elif option == 3:
            print(self.program.getParserTable())
            print("\n")
            self.fileMenuParser()
            return
        elif option == 4:
            self.program.parse(self.promptForNonTerminal())
            print("\n")
            self.fileMenuParser()
            return
        elif option == 5:
            self.program.scanSourceCode()
            print("\n")
            self.fileMenuParser()
            return
        elif option == 6:
            self.program.parserPIF()
            print("\n")
            self.fileMenuParser()
            return
        else:
            self.start()

    @staticmethod
    def displaySet(key, value):
        sb = str(key) + " = { "
        for symbol in value:
            sb += str(symbol) + ", "
        sb += "}"

        sb1 = sb[:-2]
        print(sb+"\n")

    @staticmethod
    def promptForSequence():
        input1 = input("Give the sequence:")
        input1 = input1.replace("\n", "")
        return input1.split(" ")

    @staticmethod
    def promptForNonTerminal():
        input1 = input("Give the nonTerminal:")
        return input1.strip()
