import re
import typing as typ
from collections import Counter
from enum import Enum
from copy import deepcopy

COEFFICIENT_PATTERN = r"[+-]?[0-9]*"
LITERALS_PATTERN = r"[a-z]"
EXPONENT_PATTERN = r"[a-z]\^[1-9]*"
ONES = ["", "+"]
NEGATIVE_ONE = "-"
POLYNOMIAL_PARSING_PATTERN = r"[+-]?[0-9]*[a-z\^0-9]+"


class MonomialExpressionWithoutLiteralsError(Exception):
    pass


class MonomialSign(Enum):
    POSITIVE = "+"
    NEGATIVE = "-"


class Monomial:
    def __init__(self, coefficient: int = None, variables: dict = None):
        """The 'variables' arg is a dict that will have the variables and their
        matching exponent"""
        self.coefficient = coefficient
        self.variables = variables
        self.sign = self._signum()

    @classmethod
    def from_string(cls, expression: str):
        coefficient: int = 0
        variables: dict = {}

        coefficient_expression = re.search(COEFFICIENT_PATTERN, expression)
        """
        Depending on the role and position of the Monomial (it could be
        presented just as a Monomial or within a Polynomial, and if it's
        within a Polynomial it could the first term or any subsequent) the
        coefficient 1 could be an empty string ("") or ("+", "-"), i.e:
        "a^2b^3+a^3b^2", in this example the first term has a coefficient
        of 1 and no sign in front of it, the second term has also a
        coefficient of 1 but its sign it's "+" because of the position
        """
        if coefficient_expression.group() in ONES:
            coefficient = 1
        elif coefficient_expression.group() is NEGATIVE_ONE:
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

    def __eq__(self, other: object) -> bool:
        """Compares 2 Monomials"""
        if not isinstance(other, Monomial):
            raise Exception("Error: <other> is not of a 'Monomial' instance")
        return (
            self.coefficient == other.coefficient and self.variables == other.variables
        )

    def __add__(self, other: "Monomial") -> "Monomial":
        """Adds 2 Monomials using the '+' operator"""
        if not self._alike_monomies(other):
            # Here we need to create a Polynomial
            return Polynomial([self, other])
        return Monomial(self.coefficient + other.coefficient, self.variables)

    def __sub__(self, other: "Monomial") -> "Monomial":
        """Adds 2 Monomials using the '-' operator"""
        if not self._alike_monomies(other):
            """
            Here we need to create a Polynomial if both Minuend and
            Subtrahend are not alike terms
            """
            subtrahend = deepcopy(other)
            return Polynomial([self, subtrahend.opposite()])
        return Monomial(self.coefficient - other.coefficient, self.variables)

    def __mul__(self, other: "Monomial") -> "Monomial":
        """
        Multiplies 2 Monomials
        """
        result = Monomial(
            self.coefficient * other.coefficient,
            dict(Counter(self.variables) + Counter(other.variables)),
        )
        return result

    def __truediv__(self, other: "Monomial") -> "Monomial":
        """
        Divides 2 Monomials
        """
        raw_coefficient_division = (
            self.coefficient / other.coefficient
        )  # here we get a float
        coefficient = (
            int(self.coefficient / other.coefficient)
            if raw_coefficient_division.is_integer()
            else self.coefficient / other.coefficient
        )  # here we remove the decimal part if the result is an int and we leave it if it's not
        self._sanitize_when_exponent_is_zero(
            dict(Counter(self.variables) - Counter(other.variables))
        )
        result = Monomial(coefficient, self.variables)
        return result

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
            return ""
        elif self.coefficient == -1:
            return "-"
        else:
            return str(self.coefficient)

    def _sanitize_when_exponent_is_zero(self, variables: dict) -> None:
        """
        Method used specially in Monimial Division, as we all know when two
        Monomials are divided their literal's exponents are substracted, if the
        result of that substraction is 0 then the literal 'disappears' (sorry,
        this is probably not mathematically correct to say), i.e 4ab / 2a = 2b
        """
        self.variables = {
            key: value for key, value in variables.items() if not value == 0
        }

    def _signum(self) -> MonomialSign:
        return (
            MonomialSign.POSITIVE if self.coefficient > 0 else MonomialSign.NEGATIVE
        )  # coefficient is either > 1 or < -1 never 0

    def opposite(self) -> "Monomial":
        """
        Returns the Monomial opposite by making its coefficient opposite and
        assigning the proper signum
        """
        self.coefficient = -self.coefficient
        self.sign = self._signum()
        return self


class Polynomial:
    def __init__(self, monomial_list: list[Monomial]):
        self.monomial_list: list[Monomial] = monomial_list

    @classmethod
    def from_string(cls, expression: str) -> "Polynomial":
        monomial_string_list: list = re.findall(POLYNOMIAL_PARSING_PATTERN, expression)
        monomial_list: typ.List[Monomial] = [
            Monomial.from_string(monomial_string)
            for monomial_string in monomial_string_list
        ]
        return cls(monomial_list)

    def __eq__(self, other) -> bool:
        """
        Returns true is 2 Polynomials are equals
        """
        return self.monomial_list == other.monomial_list

    def __repr__(self) -> str:
        """
        Textual representation of a Polynomial

        Note for the further improvement:

        For now if our Polynomial starts with a positive sign we remove it,
        perhaps we can improve this in the future and directly return the
        appropriate representation of the Polynomial without the need of
        stripping the string depending on the first term's sign
        """
        output = "".join(
            [
                monomial.sign.value + str(monomial)
                if monomial.sign == MonomialSign.POSITIVE
                else str(monomial)
                for monomial in self.monomial_list
            ]
        )
        if output.startswith(MonomialSign.POSITIVE.value):
            output = output[1:]

        return output

    def order_on(self, variable: str, descending: bool = True) -> "Polynomial":
        """
        Orders the Polynomial ascendingly or descendingly by the
        specified variable, if the variable is not present in the Polynomial
        it will raise an Exception
        """
        if not variable:
            raise ValueError("Variable must be specified for ordering the Polynomial")

        ordered_monomial_list = sorted(
            self.monomial_list,
            key=lambda monomial: monomial.variables.get(variable, 0),
            reverse=descending,
        )
        return Polynomial(ordered_monomial_list)

    def __add__(self, other):
        raise NotImplementedError(
            "Addition of Polynomials is not implemented yet."
        )

    def __sub__(self, other):
        raise NotImplementedError(
            "Subtraction of Polynomials is not implemented yet."
        )

    def __mul__(self, other):
        raise NotImplementedError(
            "Multiplication of Polynomials is not implemented yet."
        )

    def __truediv__(self, other):
        raise NotImplementedError(
            "Division of Polynomials is not implemented yet."
        )