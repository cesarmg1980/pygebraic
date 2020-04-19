class AlgebraicTerm():
    def __init__(self, expression):
        self.coeficient = 1
        self.literals = {}
        self.component_list = [e for e in expression]
        literal_index = 0
        for elem in self.component_list:
            if elem.isdigit():
                self.coeficient *= int(elem)
            elif elem.isalpha():
                literal_key = 'literal_' + str(literal_index)
                self.literals[literal_key] = elem
                literal_index += 1

    def __str__(self):
        str_value = str(self.coeficient) if self.coeficient is not 1 else ''
        for v in self.literals.values():
            str_value += v
        return str_value
