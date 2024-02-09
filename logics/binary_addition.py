from logics.binary_format import BinaryFormat


class BinaryAddition:
    FORMATTER = BinaryFormat()
    
    def perform(self, binary1: str, binary2: str) -> str:            
        if '.' in binary1 and '.' not in binary2:
            binary2 = binary2 + '.0000'
        
        if '.' in binary2 and '.' not in binary1:
            binary1 = binary1 + '.0000'
            
        binary1 = self.FORMATTER.perform(binary=binary1)
        binary2 = self.FORMATTER.perform(binary=binary2) 
        
        binary1, binary2 = self.FORMATTER.balance_two_binaries(binary1, binary2)    
            
        result = self.add(binary1, binary2)
        
        return result
    
    def add(self, binary1: str, binary2: str) -> str:
        carry = '0'
        result = ''

        for idx in range(len(binary1) - 1, -1, -1):
            bit1 = binary1[idx]
            bit2 = binary2[idx]
            
            if (bit1 in ' .') or (bit2 in ' .'):
                result = f'{bit1}{result}'
                continue

            if (bit1 == '1') and (bit2 == '1'):
                if carry == '1':
                    result = f'1{result}'
                else:
                    carry = '1'
                    result = f'0{result}'

                continue
            
            elif (bit1 == '1') or (bit2 == '1'):
                if carry == '1':
                    result = f'0{result}'
                else:
                    result = f'1{result}'
                
                continue
            
            else:
                if carry == '1':
                    carry = '0'
                    result = f'1{result}'
                else:
                    result = f'0{result}'

        if binary1[0] == '1' and binary2[0] == '1':
            if carry == '1':
                carry = '0'
                result = f'1{result}'
        
        elif binary1[0] == '0' and binary2[0] == '0':
            if result[0] == '1':
                result = f'0{result}'
            
        result = self.FORMATTER.perform(result)
        
        return result
    
    @staticmethod
    def get_name() -> str:
        return 'Addition'