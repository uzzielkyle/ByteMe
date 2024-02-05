class BinaryDivision:
    @staticmethod
    def perform(binary_num1, binary_num2):
        try:
            sign1 = 1 if binary_num1[0] == '0' else -1
            sign2 = 1 if binary_num2[0] == '0' else -1
            
            num1 = int(binary_num1, 2) * sign1
            num2 = int(binary_num2, 2) * sign2
            
            quotient = num1 // num2
            remainder = num1 % num2
            
            quotient_binary = bin(abs(quotient))[2:]
            remainder_binary = bin(abs(remainder))[2:]
            
            if quotient < 0:
                quotient_binary = '-' + quotient_binary
                
            return f"Quotient: '{quotient_binary}', Remainder: '{remainder_binary.zfill(len(binary_num2) - 1)}'"
        except ZeroDivisionError:
            return "error: Division by Zero."
        
    @staticmethod
    def get_name():
        return 'Division'
