from logics.from_binary import FromBinary
from logics.from_decimal import FromDecimal
from logics.binary_format import BinaryFormat

class BinaryMultiplication:
    @staticmethod
    def perform(binary1: str, binary2: str) -> str:
        binary1, binary2 = BinaryFormat().balance_two_binaries(binary1, binary2)
        
        num1 = float(FromBinary().to_decimal(binary1))
        num2 = float(FromBinary().to_decimal(binary2))
        
        product = str(num1 * num2)
        
        result = FromDecimal().to_binary(product)
        result = BinaryFormat().perform(result)
        
        return result

    @staticmethod
    def get_name() -> str:
        return 'Multiplication'
