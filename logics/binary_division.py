from logics.from_binary import FromBinary
from logics.from_decimal import FromDecimal
from logics.binary_format import BinaryFormat


class BinaryDivision:
    @staticmethod
    def perform(binary1: str, binary2: str) -> str:
        try:
            binary1, binary2 = BinaryFormat().balance_two_binaries(binary1, binary2)

            num1 = float(FromBinary().to_decimal(binary1))
            num2 = float(FromBinary().to_decimal(binary2))

            quotient = str(num1 / num2)

            result = FromDecimal().to_binary(quotient)
            result = BinaryFormat().perform(result)

            return result
        except ZeroDivisionError:
            return repr(ZeroDivisionError)

    @staticmethod
    def get_name() -> str:
        return 'Division'
