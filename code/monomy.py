import re

COEFFICIENT_PATTERN = r"-?[0-9]?"
LITERALS_PATTERN = r"[a-z]"
EXPONENT_PATTERN = r"[a-z]\^[1-9]*"
ONE = ""
MINUS_ONE = "-"


class MonomicExpressionWithoutLiteralsError(Exception):
    pass


class Monomy:
    def __init__(self, expression):
        self.coefficient = 0
        self.literals_list = []
        self.literal_to_exponent_mapping = {}
        self._build_monomy(expression)

    def _build_monomy(self, expression):
        coefficient = re.search(COEFFICIENT_PATTERN, expression)
        if coefficient.group() is ONE:
            self.coefficient = 1
        elif coefficient.group() is MINUS_ONE:
            self.coefficient = -1
        else:
            self.coefficient = int(coefficient.group())

        literals = re.findall(LITERALS_PATTERN, expression)
        if literals is None:
            raise MonomicExpressionWithoutLiteralsError

        self.literals_list = [item for item in literals]

        """the exponent list also has the exponent's literal
        this is done so you can know to what literal
        an exponent belongs
        """
        exponents_list = re.findall(EXPONENT_PATTERN, expression)
        exponents_dict = self._sanitize_exponents_list_into_dict(exponents_list)

        for literal in self.literals_list:
            self.literal_to_exponent_mapping[literal] = exponents_dict.get(literal, 1)

    def _sanitize_exponents_list_into_dict(self, exponents_list):
        """
        this should be tried differently, i don't like
        splitting the literal and exponent into a list,
        i would prefer a tuple, i'll leave it for now...
        """
        literal_exponent_dict = {}

        for element in exponents_list:
            literal_exponent_pair = element.split("^")
            literal_exponent_dict[literal_exponent_pair[0]] = int(
                literal_exponent_pair[1]
            )

        return literal_exponent_dict

    def _literal_to_exponent_mapping_to_string(self) -> str:
        """Converts the 'literal_to_exponent_mapping' into a readable string"""
        return "".join(
            [
                f"{k}^{v}" if v > 1 else f"{k}"
                for k, v in self.literal_to_exponent_mapping.items()
            ]
        )

    def _coefficient_to_string(self) -> str:
        """Converts the Monomy Coefficient to readable string"""
        if self.coefficient == 1:
            return ONE
        elif self.coefficient == -1:
            return MINUS_ONE
        else:
            return str(self.coefficient)

    def __add__(self, other: "Monomy") -> "Monomy":
        """Adds 2 Monomies using the '+' operator"""
        pass

    def __eq__(self, other: object) -> bool:
        """Compares 2 Monomies"""
        if not isinstance(other, Monomy):
            raise Exception("Error: <other> is not of a 'Monomy' instance")
        return (
            self.coefficient == other.coefficient
            and self.literals_list == other.literals_list
            and self.literal_to_exponent_mapping == other.literal_to_exponent_mapping
        )

    def __repr__(self) -> str:
        """Returns the textual representation of a Monomy"""
        return "".join(
            [
                self._coefficient_to_string(),
                self._literal_to_exponent_mapping_to_string(),
            ]
        )
