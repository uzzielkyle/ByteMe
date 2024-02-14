from logics.binary_negative import BinaryNegative
from logics.binary_addition import BinaryAddition


class BinarySubtraction:
    def perform(self, binary1: str, binary2: str) -> str:       
        result = BinaryAddition().perform(binary1, BinaryNegative().perform(binary2))
        
        return result
    
    @staticmethod
    def get_name() -> str:
        return 'Subtraction'