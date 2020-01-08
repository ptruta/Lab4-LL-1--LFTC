class Production:

    def __init__(self, start, rules):
        self.start = start
        self.rules = rules

    def getStart(self):
        return self.start

    def getRules(self):
        return self.rules

    def __str__(self):
        stri = ""
        stri += self.start + "->"
        for rule in self.rules:
            for element in rule:
                stri += element + " "
            stri += "| "
        stri1 = stri[:-2]
        return stri1
