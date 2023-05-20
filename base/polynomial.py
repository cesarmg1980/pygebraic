import typing as typ
from base.monomial import Monomial, MonomialSign


class Polynomial:
    def __init__(self, monomial_list: typ.List[Monomial]):
        self.monomial_list: typ.List[Monomial] = monomial_list

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
