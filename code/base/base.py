import re

class AlgebraicTerm():
    COEFICIENT_PATTERN = r'^\d+(?=[a-zA-Z])'
    LITERALS_PATTERN = r'([a-zA-Z]\^\d+)|([a-zA-Z])'
    
    def __init__(self, expression):
        coef = re.search(self.COEFICIENT_PATTERN, expression)
        self.coeficient = int(coef.group()) if coef is not None else 1
        literals = re.findall(self.LITERALS_PATTERN, expression)
        self.literals = {}
        literal_index = 0

        for elem in literals:
            if elem[0] is not '':
                literal_key = 'literal_' + str(literal_index) 
                self.literals[literal_key] = {}
                lit, exp = elem[0].split('^')
                self.literals[literal_key]['literal'] = lit
                self.literals[literal_key]['exponent'] = int(exp)

            else:
                literal_key = 'literal_' + str(literal_index)
                self.literals[literal_key] = {}
                self.literals[literal_key]['literal'] = elem[1]
                self.literals[literal_key]['exponent'] = 1
            literal_index += 1

    def __str__(self):
        pass
