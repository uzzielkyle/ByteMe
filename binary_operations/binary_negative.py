class BinaryNegative:
    inversion = {
        '0': '1',
        '1': '0',
    }

    def perform(self, binary: str) -> str:
        binary = binary.replace(' ', '') # remove spaces
            
        # removing decimal point if there is
        binary = binary.split('.')
        point_position: int | None = None
        
        # padding with zeros
        if len(binary) == 2:
            binary_whole_length = len(binary[0])
            binary_fraction_length = len(binary[1])
            
            binary_whole_padding_amount = 0
            binary_fraction_padding_amount = 0
            
            while (binary_whole_length % 4) != 0:
                binary_whole_padding_amount += 1
                binary_whole_length += 1
            
            point_position = binary_whole_length // 4  # places decimal point after all whole bytes
                        
            while (binary_fraction_length % 4) != 0:
                binary_fraction_padding_amount += 1
                binary_fraction_length += 1
              
            if (binary_whole_length-binary_fraction_padding_amount % 4) != 0:  
                if binary[0][0] == '0':   
                    binary[0] = binary[0].zfill(binary_whole_length)
                else:
                    binary[0] = ('1' * binary_whole_padding_amount) + binary[0]
                
            binary[1] = binary[1] + ('0' * binary_fraction_padding_amount)
            
            binary = f'{binary[0]}{binary[1]}'
            binary_length = len(binary)
            
        else:
            binary_length = len(binary[0])
            
            while (binary_length % 4) != 0:
                binary_length += 1
                
            binary = binary[0].zfill(binary_length)

        # doing the inversion
        result: str = ''
        flip: bool = False
        
        for idx in range(binary_length - 1, -1, -1):
            bit: str = binary[idx]
            if not flip:
                result = f'{bit}{result}'
                
                if bit == '1':
                    flip = True 
    
                continue
            
            result = f'{self.inversion[bit]}{result}'
                    
        # inserting decimal point
        if point_position:
            result = [(result[idx:idx+4]) for idx in range(0, len(result), 4)]
            
            result_whole = ''.join(result[:point_position])
            result_whole = self.format(result_whole)
            
            result_fraction = ''.join(result[point_position:])
            result_fraction = self.format(result_fraction)            
            
            result = f'{result_whole}.{result_fraction}'
            
        else:
            result = self.format(result)        
            
        return result
    
    @staticmethod
    def format(binary):
        result = ''
        for idx in range(0, len(binary), 4):
            result += f'{binary[idx: idx+4]} '
        
        result = result.strip()
        
        return result
        
    @staticmethod
    def get_name():
        return "Negative (Two's Complement)"