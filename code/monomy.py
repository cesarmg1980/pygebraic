import re

COEFFICIENT_PATTERN = r"^-?[0-9]"
LITERALS_PATTERN = r"[a-z]"
EXPONENT_PATTERN = r"[a-z]\^[1-9]+"


class MonomicExpressionWithoutLiteralsError(Exception):
    pass


class Monomy:
    def __init__(self, expression):
        self.monomy_coeficient = 1
        self.literals_list = []
        self.literal_to_exponent_mapping = {}
        self._build_monomy(expression)

    def _build_monomy(self, expression):
        coefficient = re.search(
            COEFFICIENT_PATTERN, expression
        )
        if coefficient is not None:
            self.monomy_coeficient = int(coefficient.group())

        literals = re.findall(
            LITERALS_PATTERN, expression
        )
        if literals is None:
            raise MonomicExpressionWithoutLiteralsError

        self.literals_list = [item for item in literals]


        """the exponent list also has the exponent's literal
        this is done so you can know to what literal
        an exponent belongs
        """
        exponents_list = re.findall(
            EXPONENT_PATTERN,
            expression
        )
        exponents_dict = self._sanitize_exponents_list_into_dict(
            exponents_list
        )

        for literal in self.literals_list:
            self.literal_to_exponent_mapping[literal] = \
                    exponents_dict.get(literal, 1)


    def _sanitize_exponents_list_into_dict(self, exponents_list):
        """
        this should be tried differently, i don't like
        splitting the literal and exponent into a list,
        i would prefer a tuple, i'll leave it for now...
        """
        literal_exponent_dict = {}

        for element in exponents_list:
            literal_exponent_pair = element.split('^')
            literal_exponent_dict[literal_exponent_pair[0]] = int(literal_exponent_pair[1])

        return literal_exponent_dict
