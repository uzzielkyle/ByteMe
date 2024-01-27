class BinaryAddition:
    @staticmethod
    def perform(binary_num1, binary_num2):
        max_len = max(len(binary_num1), len(binary_num2))
        binary_num1 = binary_num1.zfill(max_len)
        binary_num2 = binary_num2.zfill(max_len)
        
        result = ''
        carry = 0
        
        for i in range(max_len - 1, -1, -1):
            bit_sum = int(binary_num1[i]) + int(binary_num2[i]) + carry
            carry = bit_sum // 2
            result = str(bit_sum % 2) + result
        
        if carry: 
            result = '1' + result
            
        return result
    
    @staticmethod
    def get_name():
        return 'Addition'