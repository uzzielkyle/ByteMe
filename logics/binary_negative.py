from logics.binary_format import BinaryFormat


class BinaryNegative:
    INVERSION = {
        '0': '1',
        '1': '0',
    }
    FORMATTER = BinaryFormat()
    
    def perform(self, binary: str) -> str:
        binary = self.FORMATTER.perform(binary=binary) # add paddings

        result = self.invert(binary=binary)   
            
        return result
    
    def invert(self, binary: str) -> str:        
        result: str = ''
        flip: bool = False
        
        for idx in range(len(binary) - 1, -1, -1):
            bit: str = binary[idx]
            
            if bit in ' .':
                result = f'{bit}{result}'
                continue
            
            if not flip:
                result = f'{bit}{result}'
                
                if bit == '1':
                    flip = True 
    
                continue
            
            result = f'{self.INVERSION[bit]}{result}'
            
        return result
    
    @staticmethod
    def get_name() -> str:
        return "Two's Complement"