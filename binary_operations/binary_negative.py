class BinaryNegative:
    inversion = {
        '0': '1',
        '1': '0',
    }

    def perform(self, binary: str) -> str:
        binary = binary.replace(' ', '') # remove spaces
        
        # check if it has fraction
        point_position: int | None = None
        try:
            point_position = binary.index('.') + 1
        except:
            pass
            
        # removing decimal point
        binary = binary.split('.')
        
        # padding with zeros
        if len(binary) == 2:
            binary_whole_length = len(binary[0])
            binary_fraction_length = len(binary[1])
            
            binary_whole_padding_amount = binary_whole_length % 4
            binary_whole_length += binary_whole_padding_amount
            
            binary_fraction_padding_amount = binary_fraction_length % 4
            point_position += binary_fraction_padding_amount
                
            binary[0] = binary[0].zfill(binary_whole_length)
            binary[1] = binary[1] + ('0' * binary_fraction_padding_amount)
            
            binary = f'{binary[0]}{binary[1]}'
            binary_length = len(binary)
            
        else:
            binary_length = len(binary[0])
            binary_length += binary_length % 4
                
            binary = binary[0].zfill(binary_length)

        # doing the inversion
        result: str = ''
        flip: bool = False
        
        for idx in range(binary_length - 1, -1, -1):
            bit: str = binary[idx]
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
        
        # inserting decimal point
        if point_position:
            result_whole = result[:point_position].strip()
            result_fraction = result[point_position:].strip()
            
            result = f'{result_whole}.{result_fraction}'
        
        result = result.strip() # to remove leading space(s)
        
        return result
    
    @staticmethod
    def get_name():
        return "Negative (Two's Complement)"