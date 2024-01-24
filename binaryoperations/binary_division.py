from binaryoperations.binary_operation import *

class BinaryDivision:
    @staticmethod
    def perform(binary_num1, binary_num2):
        try:
            result = bin(int(binary_num1, 2) // int(binary_num2, 2))[2:]
            return result
        except ZeroDivisionError:
            return "Error: Division by zero"

    @staticmethod
    def get_name():
        return 'Division'
