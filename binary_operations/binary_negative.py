class BinaryNegative:
    inversion = {
        '0': '1',
        '1': '0',
    }

    def perform(self, binary: str) -> str:
        binary = binary.replace(' ', '')
        binary_length = len(binary)
        
        while (binary_length % 4) != 0:
            binary_length += 1
            
        binary = binary.zfill(binary_length)

        result = ''
        flip = False
        
        for idx in range(binary_length - 1, -1, -1):
            bit = binary[idx]
            if not flip:
                if (idx % 4) == 0:
                    result = f' {bit}{result}' # To separate by bytes
                else:
                    result = f'{bit}{result}'
                
                if bit == '1':
                    flip = True 
    
                continue
            
            if (idx % 4) == 0:
                result = f' {self.inversion[bit]}{result}' # To separate by bytes
                continue
            
            result = f'{self.inversion[bit]}{result}'
                
        result = result.strip() # to remove leading space(s)
        
        return result
    
    @staticmethod
    def get_name():
        return "Negative (Two's Complement)"