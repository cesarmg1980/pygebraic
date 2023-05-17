import re
from collections import Counter

COEFFICIENT_PATTERN = r"-?[0-9]*"
LITERALS_PATTERN = r"[a-z]"
EXPONENT_PATTERN = r"[a-z]\^[1-9]*"
ONE = ""
MINUS_ONE = "-"


class MonomialExpressionWithoutLiteralsError(Exception):
    pass


class Monomial:
    def __init__(self, coefficient: int = None, variables: dict = None):
        """The 'variables' arg is a dict that will have the variables and their
        matching exponent"""
        self.coefficient = coefficient
        self.variables = variables

    @classmethod
    def from_string(cls, expression: str):
        coefficient: int = 0
        variables: dict = {}

        coefficient_expression = re.search(COEFFICIENT_PATTERN, expression)
        if coefficient_expression.group() is ONE:
            coefficient = 1
        elif coefficient_expression.group() is MINUS_ONE:
            coefficient = -1
        else:
            coefficient = int(coefficient_expression.group())

        variables_list = re.findall(LITERALS_PATTERN, expression)
        if variables_list is None:
            raise MonomicExpressionWithoutLiteralsError

        variable_to_exponent_mapping = Monomial.map_exponents_to_variables(
            re.findall(EXPONENT_PATTERN, expression)
        )
        for variable in [variable for variable in variables_list]:
            variables[variable] = variable_to_exponent_mapping.get(variable, 1)

        return cls(coefficient, variables)

    @classmethod
    def map_exponents_to_variables(self, exponents_list):
        """
        Perhaps this can be tried differently since now this method is beind
        called from a classmethod it has to also a classmethod, otherwise it
        cannot be called... for now...
        """
        variable_exponent_dict = {}

        for element in exponents_list:
            variable_exponent_pair = element.split("^")
            variable_exponent_dict[variable_exponent_pair[0]] = int(
                variable_exponent_pair[1]
            )

        return variable_exponent_dict

    def __add__(self, other: "Monomial") -> "Monomial":
        """Adds 2 Monomies using the '+' operator"""
        if not self._alike_monomies(other):
            # Here we need to create a Polynomial
            raise NotImplementedError(
                "Sum of Non-Alike Monomies is not Implemented Yet"
            )
        return Monomial(self.coefficient + other.coefficient, self.variables)

    def __sub__(self, other: "Monomial") -> "Monomial":
        """Adds 2 Monomies using the '+' operator"""
        if not self._alike_monomies(other):
            # Here we need to create a Polynomial
            raise NotImplementedError(
                "Sum of Non-Alike Monomies is not Implemented Yet"
            )
        return Monomial(self.coefficient - other.coefficient, self.variables)

    def __mul__(self, other: "Monomial") -> "Monomial":
        """
        Multiplies 2 Monomials
        """
        return Monomial(
            self.coefficient * other.coefficient,
            dict(Counter(self.variables) + Counter(other.variables)),
        )

    def __eq__(self, other: object) -> bool:
        """Compares 2 Monomies"""
        if not isinstance(other, Monomial):
            raise Exception("Error: <other> is not of a 'Monomial' instance")
        return (
            self.coefficient == other.coefficient and self.variables == other.variables
        )

    def __repr__(self) -> str:
        """Returns the textual representation of a Monomial"""
        return "".join(
            [
                self._coefficient_to_string(),
                self._variables_to_string(),
            ]
        )

    def _alike_monomies(self, other: "Monomial") -> bool:
        """Returns True whether the 2 Monomials are alike (have same literal
        parts)"""
        return self.variables == other.variables

    def _variables_to_string(self) -> str:
        """Converts the 'literal_to_exponent_mapping' into a readable string"""
        return "".join(
            [f"{k}^{v}" if v > 1 else f"{k}" for k, v in self.variables.items()]
        )

    def _coefficient_to_string(self) -> str:
        """Converts the Monomial Coefficient to readable string"""
        if self.coefficient == 1:
            return ONE
        elif self.coefficient == -1:
            return MINUS_ONE
        else:
            return str(self.coefficient)
