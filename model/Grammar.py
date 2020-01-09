from model.Production import Production


class Grammar:

    def __init__(self):
        self.N = []
        self.E = []
        self.P = []
        self.S = ""
        self.read_from_file()

    def is_non_terminal(self, value):
        if value in self.N:
            return True
        return False

    def is_terminal(self, value):
        if value in self.E:
            return True
        return False

    def read_from_file(self):
        try:
            i = 0
            with open('./data/grammar1') as f:
                for line in f.readlines():
                    if i <= 2:
                        line = line.replace("\n", "")
                        tokens = line.split(" ")
                        for j in range(0, len(tokens), 1):
                            if i == 0:
                                self.N.append(tokens[j])
                            if i == 1:
                                self.E.append(tokens[j])
                            if i == 2:
                                self.S = tokens[j]
                    if i > 2:
                        line = line.strip("\n")
                        tokens = line.split(" -> ")
                        rules = []

                        print(tokens)

                        for rule in tokens[1].split(" | "):
                            rules.append(rule.split(" "))

                        self.P.append(Production(tokens[0], rules))

                    i = i + 1

        except IOError as e:
            print(e)

    def get_productions_for_non_terminal(self, non_terminal):
        if not self.is_non_terminal(non_terminal):
            raise Exception('Can only show productions for non-terminals')

        ls = [prod for prod in self.P if prod.getStart() == non_terminal]
        return ls

    def get_productions_containing_non_terminal(self, non_terminal):
        if not self.is_non_terminal(non_terminal):
            raise Exception('Can only show productions for non-terminals')

        ls = [prod for prod in self.P for rule in prod.getRules() if non_terminal in rule]
        return ls

    def get_productions(self):
        return self.P

    def get_non_terminals(self):
        return self.N

    def get_terminals(self):
        return self.E

    def get_starting_symbol(self):
        return self.S

    def __str__(self):
        return 'N = { ' + ', '.join(self.N) + ' }\n' \
               + 'E = { ' + ', '.join(self.E) + ' }\n' \
               + 'P = { ' + ', '.join([' -> '.join(prod) for prod in self.P]) + ' }\n' \
               + 'S = ' + str(self.S) + '\n'
